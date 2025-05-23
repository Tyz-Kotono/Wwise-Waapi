from WaapiCore import *
from QTUI import *

from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtCore import QEvent as QEventType
import sys


class MainWindow:
    def __init__(self):

        self.window = QTMainWindow("Wwise Tool")
        self.window.resize(300, 200)
        self.window.show()
        InitWindow(self.window)


def InitWindow(window):
    window.AddCallBackEvent(QEventType.Type.Enter, [lambda: print("Enter")])
    # window.AddCallBackEvent(QEventType.Type.Enter, [WaapiData.Update])

    window.AddCallBackEvent(QEventType.Type.Leave, [lambda: print("Leave")])
    window.statusBar().showMessage("Window Initialized")
