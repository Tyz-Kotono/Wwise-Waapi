from WaapiCore import WaapiData
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PySide6.QtCore import Qt
import sys


class QTMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDockWidget 任意堆叠（九宫格）")
        self.setDockNestingEnabled(True)

        # 状态栏用于显示Debug信息
        self.statusBar().showMessage("Ready")

        # 创建四个 dock
        dock1a = QDockWidget("Dock 1", self)
        dock1a.setWidget(QTextEdit("内容 1"))
        dock2a = QDockWidget("Dock 2", self)
        dock2a.setWidget(QTextEdit("内容 2"))
        dock1b = QDockWidget("Dock 3", self)
        dock1b.setWidget(QTextEdit("内容 3"))
        dock2b = QDockWidget("Dock 4", self)
        dock2b.setWidget(QTextEdit("内容 4"))

        for dock in [dock1a, dock2a, dock1b, dock2b]:
            dock.setFeatures(
                QDockWidget.DockWidgetMovable
                | QDockWidget.DockWidgetFloatable
                | QDockWidget.DockWidgetClosable
            )

        self.addDockWidget(Qt.LeftDockWidgetArea, dock1a)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2a)
        self.addDockWidget(Qt.TopDockWidgetArea, dock1b)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock2b)

    def enterEvent(self, event):
        # 在状态栏显示Debug信息
        self.statusBar().showMessage("Enter")
        print("Enter")  # 控制台也输出
        super().enterEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTMainWindow()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
