#!/usr/bin/env python3
# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects.html


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStyle,
    QVBoxLayout,
    QWidget,
    QDockWidget,
    QApplication,
    QMainWindow,
    QDockWidget,
    QVBoxLayout,
    QWidget,
    QStyle,
)
import sys

from Wwise_UI import *
from QTSelectMenu import *
from WappiCommon import *
from QTSelectMenu import *
from PySide6.QtCore import Qt
from pprint import pprint


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        InitWappi()
        self.setWindowTitle("QTSelectMenu 测试")

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)
        icon = app.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)

        # Menu and OpenButton
        self.btn = QSelectMenuToolButton(
            self,
            commonOpstionsReturn,
            defaultOpstionsReturn,
            icon=icon,
            CallBack=SetSelectOptions,
        )

        layout.addWidget(self.btn)

        # 获取数据
        self.table_widget = QMenuTableWidget()
        self.btn.MenuChanged(self.table_widget.UpdateTable)

        # 创建QDockWidget并放入table_widget
        self.dock = QDockWidget("对象列表", self)
        self.dock.setWidget(self.table_widget)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock)

    def closeEvent(self, event):
        super().closeEvent(event)
        WwiseDataInstance().CloseClient()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestWindow()
    win.resize(300, 200)
    win.show()
    sys.exit(app.exec())
