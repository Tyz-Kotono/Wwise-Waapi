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
import sys


class SearchBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(8)



        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("搜索...")
        layout.addWidget(self.search_edit, stretch=1)

        self.btn1 = QToolButton()
        self.btn1.setIcon(QIcon.fromTheme("document-new"))
        self.btn1.setIconSize(QSize(20, 20))
        layout.addWidget(self.btn1)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("带Dock的SearchBar示例")
    main_win.resize(600, 400)

    # 创建Dock内容容器
    dock_content = QWidget()
    vlayout = QVBoxLayout(dock_content)
    vlayout.setContentsMargins(0, 0, 0, 0)
    vlayout.setSpacing(0)

    # 创建SearchBar并放到顶部
    bar = SearchBar()
    vlayout.addWidget(bar)

    # 下面可以放别的内容，比如一个标签
    label = QLabel("这里可以放其他内容")
    label.setAlignment(Qt.AlignCenter)
    vlayout.addWidget(label, stretch=1)

    # 创建Dock并承载容器
    dock = QDockWidget("搜索栏", main_win)
    dock.setWidget(dock_content)
    dock.setFeatures(QDockWidget.NoDockWidgetFeatures)

    main_win.addDockWidget(Qt.TopDockWidgetArea, dock)

    main_win.show()
    sys.exit(app.exec())
