from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFontMetrics


class MultiSelectWidget(QWidget):
    def __init__(self, all_options=None, default_selected=None, parent=None):
        super().__init__(parent)
        self.all_options = all_options or []
        self.selected = set(default_selected or [])

        self.layout = QVBoxLayout()
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self._build_ui()

    def _build_ui(self):
        # 清空旧的
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 重新创建选项
        for option in self.all_options:
            item = MultiSelectItem(option, option in self.selected)
            item.clicked.connect(self._on_item_clicked)
            self.layout.addWidget(item)
        self.layout.addStretch(1)

    def _on_item_clicked(self, option):
        if option in self.selected:
            self.selected.remove(option)
        else:
            self.selected.add(option)
        self._update_items()

    def _update_items(self):
        # 更新所有item的显示状态
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            if item is None:
                continue
            widget = item.widget()
            if isinstance(widget, MultiSelectItem):
                widget.set_checked(widget.option in self.selected)

    def get_selected(self):
        """返回当前选中的列表"""
        return list(self.selected)

    def set_options(self, all_options, default_selected=None):
        """切换显示的选项，重置选中"""
        self.all_options = all_options or []
        self.selected = set(default_selected or [])
        self._build_ui()


class MultiSelectItem(QWidget):
    clicked = Signal(str)

    def __init__(self, option, checked=False, parent=None):
        super().__init__(parent)
        self.option = option
        self.checked = checked

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.setLayout(self.layout)

        # 用一个固定宽度的label显示打钩符号，保持对齐
        self.check_label = QLabel()
        self.check_label.setFixedWidth(self._checkmark_width())
        self.check_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.check_label)

        self.text_label = QLabel(option)
        self.text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout.addWidget(self.text_label)

        self.set_checked(checked)

    def _checkmark_width(self):
        # 计算勾号宽度，保证所有项对齐
        fm = QFontMetrics(self.font())
        return fm.horizontalAdvance("✓") + 4  # 多留点间距

    def set_checked(self, checked):
        self.checked = checked
        if checked:
            self.check_label.setText("✓")
        else:
            self.check_label.setText("")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.option)
        super().mousePressEvent(event)


# 测试界面
class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MultiSelectWidget 测试")

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 初始选项和默认选中
        self.options1 = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
        self.default1 = ["香蕉", "西瓜"]

        self.options2 = ["红色", "绿色", "蓝色", "黄色"]
        self.default2 = ["绿色"]

        self.multi_select = MultiSelectWidget(self.options1, self.default1)
        self.main_layout.addWidget(self.multi_select)

        btn_layout = QHBoxLayout()
        self.btn_get = QPushButton("获取当前选择")
        self.btn_switch = QPushButton("切换选项")
        btn_layout.addWidget(self.btn_get)
        btn_layout.addWidget(self.btn_switch)
        self.main_layout.addLayout(btn_layout)

        self.result_label = QLabel("")
        self.main_layout.addWidget(self.result_label)

        self.btn_get.clicked.connect(self.on_get_selected)
        self.btn_switch.clicked.connect(self.on_switch_options)

        self.toggle = False

    def on_get_selected(self):
        selected = self.multi_select.get_selected()
        self.result_label.setText("当前选择: " + ", ".join(selected))

    def on_switch_options(self):
        if self.toggle:
            self.multi_select.set_options(self.options1, self.default1)
        else:
            self.multi_select.set_options(self.options2, self.default2)
        self.result_label.setText("")
        self.toggle = not self.toggle


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = TestWindow()
    w.resize(300, 300)
    w.show()
    sys.exit(app.exec())
