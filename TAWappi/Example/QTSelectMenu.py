from PySide6.QtWidgets import QMenu, QToolButton, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal

from pprint import pprint
from Wwise_UI import *
from QTSelectMenu import *
from WappiCommon import *
from QTSelectMenu import *
from WappiFunctionLibrary import *


class QTSelectMenu(QMenu):
    selectionChanged = Signal(list)  # 选中变化信号

    def __init__(
        self,
        parent=None,
        all_options=None,
        default_selected=None,
        extra_actions=None,
        selectionChangedCallBack=None,
    ):
        super().__init__(parent)
        self.all_options = all_options or []
        self.selected = set(default_selected or [])
        # [(text, checkable, checked)]
        self.extra_actions = extra_actions or []
        self.actions_map = {}  # option: QAction
        self.extra_actions_map = {}  # text: QAction
        self._build_menu()
        if selectionChangedCallBack:
            self.selectionChanged.connect(selectionChangedCallBack)

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
        return [opt for opt in self.all_options if opt in self.selected]

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
        # print("test")
        return self.extra_actions_map.get(text)


# self.btn = QPushButton("选择选项")
# self.btn.setMenu(self.menu)
# layout.addWidget(self.btn)


class QSelectMenuToolButton(QToolButton):

    def __init__(
        self,
        parent=None,
        all_options=None,
        default_selected=None,
        extra_actions=None,
        icon=None,
        CallBack=None,
    ):
        super().__init__(parent)
        self.setPopupMode(QToolButton.InstantPopup)  # 直接弹菜单
        self.Menu = QTSelectMenu(
            self, all_options, default_selected, extra_actions, CallBack
        )
        self.setMenu(self.Menu)
        self.setIcon(icon)

    def setMenu(self, menu):
        super().setMenu(menu)
        self.setText(menu.title())

    def MenuChanged(self, selection_changed):
        self.Menu.selectionChanged.connect(selection_changed)

    def GetMenuSelected(self):
        """获取当前选中的选项"""
        return [opt for opt in self.Menu.all_options if opt in self.Menu.selected]


class QMenuTableWidget(QTableWidget):

    def __init__(self, parent=None, type: WwiseListType = WwiseListType.SELECT):
        super().__init__(parent)

        self.Type: WwiseListType = type
        self.UpdateTable()

    def UpdateTable(self):
        self.clear()
        options, Datas = GetWappiData(self.Type)
        self.setRowCount(len(Datas))
        self.setColumnCount(len(Datas[0]))
        self.setHorizontalHeaderLabels(options)
        self.SetItem(options, Datas)

    def SetItem(self, options, Datas):
        for i, data_dict in enumerate(Datas):
            for j, key in enumerate(options):
                self.setItem(i, j, QTableWidgetItem(data_dict[key]))
