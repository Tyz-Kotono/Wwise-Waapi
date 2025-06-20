import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDockWidget,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QListView,
    QStyledItemDelegate,
)
from PySide6.QtCore import Qt, QTimer, Signal, QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem

from waapi import WaapiClient, CannotConnectToWaapiException

FROM_TYPES = ["id", "search", "name", "path", "ofType", "query"]

OF_TYPE_VALUES = [
    "ActorMixer",
    "AudioFileSource",
    "BlendContainer",
    "Bus",
    "Event",
    "Folder",
    "MusicSegment",
    "MusicTrack",
    "RandomContainer",
    "SequenceContainer",
    "Sound",
    "State",
    "Switch",
    "SwitchContainer",
    "WorkUnit",
]


def build_waapi_args(from_type, from_value, name_substring=""):
    args = {}
    if from_type == "name":
        if not from_value.startswith("\\"):
            return None, "name类型必须输入唯一限定名（以\\开头的全路径）"
        args["from"] = {from_type: [from_value]}
    elif from_type == "search":
        args["from"] = {from_type: [from_value]}
    elif from_type == "ofType":
        args["from"] = {from_type: [from_value]}
        if name_substring:
            args["transform"] = [{"where": ["name:contains", name_substring]}]
    else:
        args["from"] = {from_type: [from_value]}
    return args, None


def call_waapi_search(client, args):
    options = {"return": ["id", "type", "name"]}
    try:
        result = client.call("ak.wwise.core.object.get", args, options=options)
        if result and result.get("return"):
            return result["return"], None
        else:
            return [], None
    except Exception as e:
        return None, f"搜索出错: {e}"


def format_result_item(obj):
    return f"{obj['name']} ({obj['type']}) - {obj['id']}"


def get_input_placeholder(from_type):
    if from_type == "name":
        return "请输入对象的唯一限定名（如 \\Actor-Mixer Hierarchy\\Default Work Unit\\MyEvent）"
    elif from_type == "search":
        return "请输入要搜索的名字片段"
    elif from_type == "id":
        return "请输入对象的GUID或Short ID"
    elif from_type == "path":
        return "请输入对象的路径"
    elif from_type == "query":
        return "请输入对象的GUID"
    else:
        return "输入值"


class MultiSelectComboBox(QComboBox):
    # 自定义多选下拉框
    selectionChanged = Signal()

    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setModel(QStandardItemModel(self))
        self.setView(QListView(self))
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setPlaceholderText("类型过滤（多选）")
        self._items = items
        self._checked = set(items)
        self.populate()
        self.view().pressed.connect(self.handle_item_pressed)
        self.update_display_text()

    def populate(self):
        model = self.model()
        model.clear()
        for text in self._items:
            item = QStandardItem(text)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            item.setData(Qt.Checked, Qt.CheckStateRole)
            model.appendRow(item)

    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            self._checked.discard(item.text())
        else:
            item.setCheckState(Qt.Checked)
            self._checked.add(item.text())
        self.update_display_text()
        self.selectionChanged.emit()

    def checked_items(self):
        return list(self._checked)

    def set_checked_items(self, items):
        self._checked = set(items)
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            if item.text() in self._checked:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
        self.update_display_text()
        self.selectionChanged.emit()

    def update_display_text(self):
        if len(self._checked) == 0:
            self.lineEdit().setText("无")
        elif len(self._checked) == len(self._items):
            self.lineEdit().setText("全部")
        else:
            self.lineEdit().setText(", ".join(self._checked))


class WaapiDockWidget(QDockWidget):
    def __init__(self, waapi_client, parent=None):
        super().__init__("WAAPI Search", parent)
        self.waapi_client = waapi_client

        main_widget = QWidget()
        self.setWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # 第一行：from类型选择
        from_layout = QHBoxLayout()
        layout.addLayout(from_layout)
        from_layout.addWidget(QLabel("from类型:"))
        self.from_type_combo = QComboBox()
        self.from_type_combo.addItems(FROM_TYPES)
        from_layout.addWidget(self.from_type_combo)

        # 第二行：ofType下拉或文本输入
        value_layout = QHBoxLayout()
        layout.addLayout(value_layout)
        self.value_label = QLabel("值:")
        value_layout.addWidget(self.value_label)
        self.of_type_combo = QComboBox()
        self.of_type_combo.addItems(OF_TYPE_VALUES)
        value_layout.addWidget(self.of_type_combo)
        self.value_edit = QLineEdit()
        value_layout.addWidget(self.value_edit)

        # 第三行：名称包含（仅ofType时显示）
        search_layout = QHBoxLayout()
        layout.addLayout(search_layout)
        self.name_label = QLabel("名称包含:")
        search_layout.addWidget(self.name_label)
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("可选，输入名称模糊搜索")
        search_layout.addWidget(self.search_box)

        # 类型过滤多选下拉
        filter_layout = QHBoxLayout()
        layout.addLayout(filter_layout)
        filter_layout.addWidget(QLabel("类型过滤:"))
        self.type_filter_combo = MultiSelectComboBox(OF_TYPE_VALUES)
        filter_layout.addWidget(self.type_filter_combo)

        # 结果列表
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        # Timer for debounce
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.do_search)

        # 信号连接
        self.from_type_combo.currentIndexChanged.connect(self.on_from_type_changed)
        self.of_type_combo.currentIndexChanged.connect(self.on_input_changed)
        self.value_edit.textChanged.connect(self.on_input_changed)
        self.search_box.textChanged.connect(self.on_input_changed)
        self.type_filter_combo.selectionChanged.connect(self.filter_results)

        self._all_results = []
        self.on_from_type_changed(0)  # 初始化

    def on_from_type_changed(self, idx):
        from_type = self.from_type_combo.currentText()
        if from_type == "ofType":
            self.value_label.setText("类型:")
            self.of_type_combo.setVisible(True)
            self.value_edit.setVisible(False)
            self.name_label.setVisible(True)
            self.search_box.setVisible(True)
        else:
            self.value_label.setText("值:")
            self.of_type_combo.setVisible(False)
            self.value_edit.setVisible(True)
            self.value_edit.setPlaceholderText(get_input_placeholder(from_type))
            self.name_label.setVisible(False)
            self.search_box.setVisible(False)
        self.on_input_changed()

    def on_input_changed(self, *args):
        self.timer.start(300)

    def do_search(self):
        from_type = self.from_type_combo.currentText()
        if from_type == "ofType":
            from_value = self.of_type_combo.currentText()
            name_substring = self.search_box.text().strip()
        else:
            from_value = self.value_edit.text().strip()
            name_substring = ""
        self.result_list.clear()
        self._all_results = []
        if not from_value:
            return
        args, err = build_waapi_args(from_type, from_value, name_substring)
        if err:
            self.result_list.addItem(err)
            return
        results, err = call_waapi_search(self.waapi_client, args)
        if err:
            self.result_list.addItem(err)
            return
        self._all_results = results
        self.filter_results()

    def filter_results(self):
        checked_types = set(self.type_filter_combo.checked_items())
        self.result_list.clear()
        for obj in self._all_results:
            if obj["type"] in checked_types:
                self.result_list.addItem(format_result_item(obj))


class MainWindow(QMainWindow):
    def __init__(self, waapi_client):
        super().__init__()
        self.setWindowTitle("Wwise Waapi Dock Search")
        self.resize(700, 500)
        self.dock = WaapiDockWidget(waapi_client, self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)


def main():
    app = QApplication(sys.argv)
    try:
        waapi_client = WaapiClient()
    except CannotConnectToWaapiException:
        QMessageBox.critical(
            None, "错误", "无法连接到Waapi，请确保Wwise已启动并启用Waapi。"
        )
        sys.exit(1)
    window = MainWindow(waapi_client)
    window.show()
    app.exec()
    waapi_client.disconnect()


if __name__ == "__main__":
    main()
