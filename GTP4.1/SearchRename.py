import sys
import re
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDockWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QListWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt

from waapi import WaapiClient, CannotConnectToWaapiException


# --- WAAPI相关函数 ---
def search_objects_by_regex(client, regex_pattern, type_str):
    # 获取所有指定类型对象
    args = {
        "from": {"ofType": [type_str]},
        "options": {"return": ["id", "type", "name"]},
    }
    result = client.call("ak.wwise.core.object.get", args)
    if not result or "return" not in result:
        return []
    # 用正则筛选
    pattern = re.compile(regex_pattern)
    return [obj for obj in result["return"] if pattern.search(obj["name"])]


def waapi_rename(client, object_id, new_name):
    arg = {"object": object_id, "value": new_name}
    client.call("ak.wwise.core.object.setName", arg)


# --- PySide6 Dock窗口 ---
class WaapiRenameDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("WAAPI批量重命名", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.setFeatures(
            QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable
        )

        # 主体Widget
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # 正则输入
        regex_layout = QHBoxLayout()
        regex_layout.addWidget(QLabel("正则筛选:"))
        self.regex_input = QLineEdit()
        self.regex_input.setPlaceholderText("如: ^MyPrefix_.*$")
        regex_layout.addWidget(self.regex_input)
        layout.addLayout(regex_layout)

        # 行为选择
        action_layout = QHBoxLayout()
        action_layout.addWidget(QLabel("重命名行为:"))
        self.action_combo = QComboBox()
        self.action_combo.addItems(
            [
                "替换正则关键词",  # 0
                "全部加尾缀(如_01)",  # 1
                "尾缀重排(如_0, _1...)",  # 2
            ]
        )
        action_layout.addWidget(self.action_combo)
        layout.addLayout(action_layout)

        # 替换内容输入
        replace_layout = QHBoxLayout()
        replace_layout.addWidget(QLabel("重命名内容:"))
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("如: 新字符串/尾缀")
        replace_layout.addWidget(self.replace_input)
        layout.addLayout(replace_layout)

        # 类型选择
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("对象类型:"))
        self.type_input = QLineEdit("Folder")
        self.type_input.setPlaceholderText("如: Folder, Event, Sound")
        type_layout.addWidget(self.type_input)
        layout.addLayout(type_layout)

        # 搜索按钮
        self.search_btn = QPushButton("搜索")
        layout.addWidget(self.search_btn)

        # 结果列表
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        # 执行按钮
        self.rename_btn = QPushButton("批量重命名")
        layout.addWidget(self.rename_btn)

        self.setWidget(main_widget)

        # 事件绑定
        self.search_btn.clicked.connect(self.on_search)
        self.rename_btn.clicked.connect(self.on_rename)

        # WAAPI连接
        try:
            self.client = WaapiClient()
        except CannotConnectToWaapiException:
            QMessageBox.critical(self, "错误", "无法连接到WAAPI")
            self.client = None

        self.objects = []

    def on_search(self):
        if not self.client:
            QMessageBox.critical(self, "错误", "未连接到WAAPI")
            return
        regex = self.regex_input.text()
        type_str = self.type_input.text().strip()
        if not regex or not type_str:
            QMessageBox.warning(self, "提示", "请填写正则和类型")
            return
        try:
            self.objects = search_objects_by_regex(self.client, regex, type_str)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"搜索失败: {e}")
            return
        self.result_list.clear()
        for obj in self.objects:
            self.result_list.addItem(f"{obj['name']} ({obj['id']})")

    def on_rename(self):
        if not self.client or not self.objects:
            QMessageBox.warning(self, "提示", "请先搜索对象")
            return
        action = self.action_combo.currentIndex()
        content = self.replace_input.text()
        regex = self.regex_input.text()
        pattern = re.compile(regex)
        try:
            for idx, obj in enumerate(self.objects):
                old_name = obj["name"]
                new_name = old_name
                if action == 0:  # 替换正则关键词
                    new_name = pattern.sub(content, old_name)
                elif action == 1:  # 全部加尾缀
                    new_name = f"{old_name}{content}{str(idx).zfill(2)}"
                elif action == 2:  # 尾缀重排
                    base = re.sub(r"(_\d+)$", "", old_name)
                    new_name = f"{base}_{idx}"
                if new_name != old_name:
                    waapi_rename(self.client, obj["id"], new_name)
            QMessageBox.information(self, "完成", "批量重命名完成！")
            self.on_search()  # 刷新
        except Exception as e:
            QMessageBox.critical(self, "错误", f"重命名失败: {e}")


# --- 主窗口 ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wwise WAAPI 批量重命名工具")
        self.resize(600, 400)
        self.dock = WaapiRenameDock(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
