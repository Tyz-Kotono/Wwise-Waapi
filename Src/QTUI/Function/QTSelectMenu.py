from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal


class QTSelectMenu(QMenu):
    selectionChanged = Signal(list)  # 选中变化信号

    def __init__(
        self, all_options=None, default_selected=None, extra_actions=None, parent=None
    ):
        super().__init__(parent)
        self.all_options = all_options or []
        self.selected = set(default_selected or [])
        self.extra_actions = extra_actions or []  # [(text, checkable, checked)]
        self.actions_map = {}  # option: QAction
        self.extra_actions_map = {}  # text: QAction
        self._build_menu()

    def _build_menu(self):
        self.clear()
        self.actions_map.clear()
        self.extra_actions_map.clear()
        # 添加多选项
        for option in self.all_options:
            act = QAction(option, self)
            act.setCheckable(True)
            act.setChecked(option in self.selected)
            act.toggled.connect(self._on_action_toggled)
            self.addAction(act)
            self.actions_map[option] = act
        # 添加分隔线和额外项
        if self.extra_actions:
            self.addSeparator()
            for text, checkable, checked in self.extra_actions:
                act = QAction(text, self)
                act.setCheckable(checkable)
                if checkable:
                    act.setChecked(checked)
                self.addAction(act)
                self.extra_actions_map[text] = act

    def _on_action_toggled(self, checked):
        sender = self.sender()
        for opt, act in self.actions_map.items():
            if act is sender:
                if checked:
                    self.selected.add(opt)
                else:
                    self.selected.discard(opt)
                self.selectionChanged.emit(self.get_selected())
                break

    def get_selected(self):
        return list(self.selected)

    def set_options(self, all_options, default_selected=None):
        self.all_options = all_options or []
        self.selected = set(default_selected or [])
        self._build_menu()

    def set_selected(self, selected):
        self.selected = set(selected or [])
        for opt, act in self.actions_map.items():
            act.setChecked(opt in self.selected)

    def get_extra_action(self, text):
        """获取额外功能项 QAction"""
        return self.extra_actions_map.get(text)


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)
import sys


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTSelectMenu 测试")

        options1 = ["Routing", "Positioning", "General", "All"]
        default1 = ["Routing", "All"]
        # 额外功能项：(文本, 是否可勾选, 默认勾选)
        extra = [
            ("Configure Favorites...", False, False),
            ("Reset Favorites Order to Default", False, False),
            ("Always Show Additional Properties", True, True),
        ]

        self.menu = QTSelectMenu(options1, default1, extra, self)

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        self.btn = QPushButton("选择选项")
        self.btn.setMenu(self.menu)
        layout.addWidget(self.btn)

        self.label = QLabel("当前选择: " + ", ".join(self.menu.get_selected()))
        layout.addWidget(self.label)

        self.menu.selectionChanged.connect(self.on_selection_changed)

        # 监听额外可勾选项
        extra_action = self.menu.get_extra_action("Always Show Additional Properties")
        if extra_action:
            extra_action.toggled.connect(lambda checked: print("Always Show:", checked))

    def on_selection_changed(self, selected):
        self.label.setText("当前选择: " + ", ".join(selected))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestWindow()
    win.resize(350, 200)
    win.show()
    sys.exit(app.exec())
