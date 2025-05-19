from WaapiCore import *
from Core import *
from QTUI import QTMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PySide6.QtCore import Qt
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTMainWindow()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
