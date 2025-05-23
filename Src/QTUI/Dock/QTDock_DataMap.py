from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDockWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QToolButton,
    QLabel,
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt
from QTUI.Function.QTSelectMenu import QTSelectMenu
from QTUI.Function import QTSearchBar
import sys


class QTDockDataMap(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Data Map")
        self.setAllowedAreas(Qt.AllDockWidgetAreas)

        # 创建Dock内容容器
        dock_content = QWidget()
        vlayout = QVBoxLayout(dock_content)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(4)

        # 创建SearchBar并放到顶部
        bar = QTSearchBar()
        vlayout.addWidget(bar)

        # 下面可以放别的内容，比如一个标签
        label = QLabel("这里可以放其他内容")
        label.setAlignment(Qt.AlignCenter)
        vlayout.addWidget(label, stretch=1)

        # 创建Dock并承载容器

        self.setWidget(dock_content)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)
