#!/usr/bin/env python3

import sys
import os
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects.html


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDockWidget,
    QToolButton,
    QWidget,
    QVBoxLayout,
)

from Wwise_UI import *
from QTSelectMenu import *
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolButton,
    QPushButton,
    QStyle,
    QVBoxLayout,
    QWidget,
    QLabel,
)
import sys


from WappiCommon import *
from QTSelectMenu import *


class TestWindow(QMainWindow):

    def __init__(self, client):
        super().__init__()
        self.setWindowTitle("QTSelectMenu 测试")
        self.client = client

        # 额外功能项：(文本, 是否可勾选, 默认勾选)

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        # self.btn.setIcon(icon)
        icon = app.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)

        self.btn = QSelectMenuToolButton(
            all_options=defaultOpstionsReturn,
            default_selected=commonOpstionsReturn,
            extra_actions=[],
            icon=icon,
        )
        self.btn.MenuChanged(self.on_selection_changed)
        # Add Buttton

        layout.addWidget(self.btn)
        data = getSelectedObjects(
            self.client, opstions={"return": self.btn.GetMenuSelected()}
        )
        # pprint(data)

        self.label = QLabel("当前选择: " + ", ".join(self.btn.GetMenuSelected()))
        layout.addWidget(self.label)

    def on_selection_changed(self, selected):
        # data = getSelectedObjects(self.client, opstions={"return": selected})
        # pprint("获取到的选中对象:", data)
        self.label.setText("当前选择: " + ", ".join(selected))
        getSelectedObjects(self.client, opstions={"return": selected})


if __name__ == "__main__":

    app = QApplication(sys.argv)
    with WaapiClient() as client:
        win = TestWindow(client)
        win.resize(150, 80)
        win.show()

    sys.exit(app.exec())
