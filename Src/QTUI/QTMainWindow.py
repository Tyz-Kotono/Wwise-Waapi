# from WaapiCore import WaapiData
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtCore import QEvent as QEventType
import sys
from pprint import pprint

from QTUI.Dock import *


class QTMainWindow(QMainWindow):
    def __init__(self, Name: str = "Wwise Tool"):
        super().__init__()
        self.setWindowTitle(Name)
        self.setDockNestingEnabled(True)

        # 使用字典来维护事件类型和对应的回调函数列表
        self.event_callbacks = {}

        # 状态栏用于显示Debug信息
        self.statusBar().showMessage("Ready")

        # 创建四个 dock
        dock1 = QDockWidget("Dock 1", self)
        dock1.setWidget(QTextEdit("内容 1"))
        dock2 = QDockWidget("Dock 2", self)
        dock2.setWidget(QTextEdit("内容 2"))
        dock3 = QTDockDataMap(self)
        dock4 = QDockWidget("Dock 4", self)
        dock4.setWidget(QTextEdit("内容 4"))

        for dock in [dock1, dock2, dock3, dock4]:
            dock.setFeatures(
                QDockWidget.DockWidgetMovable
                | QDockWidget.DockWidgetFloatable
                | QDockWidget.DockWidgetClosable
            )

        # 添加左边 Dock 1
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        # 添加中间上方 Dock 3 到右边区域（先放右边）
        self.addDockWidget(Qt.RightDockWidgetArea, dock3)

        # 把 Dock 2 垂直分割到 Dock 3 下面
        self.splitDockWidget(dock3, dock2, Qt.Vertical)

        # 添加右边 Dock 4 到右边区域
        self.addDockWidget(Qt.RightDockWidgetArea, dock4)

        # 把 Dock 4 水平分割到 Dock 2 右边
        self.splitDockWidget(dock2, dock4, Qt.Horizontal)

    def AddCallBackEvent(self, event_type: QEventType.Type, funcs):
        if not isinstance(event_type, QEventType.Type):
            raise ValueError("event_type must be an instance of QEventType.Type")

        # 如果事件类型不存在于字典中，初始化一个新的列表
        if event_type not in self.event_callbacks:
            self.event_callbacks[event_type] = []

        # 判断 funcs 是单个函数还是函数列表
        if callable(funcs):
            self.event_callbacks[event_type].append(funcs)
        elif isinstance(funcs, list):
            for func in funcs:
                if callable(func):
                    self.event_callbacks[event_type].append(func)
                else:
                    raise ValueError("All elements in the funcs list must be callable")
        else:
            raise ValueError("funcs must be a callable or a list of callables")

    def leaveEvent(self, event):
        print("LeaveEvent")
        super().leaveEvent(event)
        LoopTriggerFunction(self.event_callbacks.get(QEventType.Type.Leave, []))

    def enterEvent(self, event):
        print("EnterEvent")
        super().enterEvent(event)
        LoopTriggerFunction(self.event_callbacks.get(QEventType.Type.Enter, []))

    def closeEvent(self, event):
        super().closeEvent(event)
        LoopTriggerFunction(self.event_callbacks.get(QEventType.Type.Close, []))


def LoopTriggerFunction(callbacks):
    [f() for f in callbacks if callable(f)]
    # for func in callbacks:
    #     if callable(func):
    #         try:
    #             func()  # 确保不传递参数
    #         except Exception as e:
    #             print(f"Error calling function {func}: {e}")
