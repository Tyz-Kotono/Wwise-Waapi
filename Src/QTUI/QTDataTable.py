from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QPushButton,
)
import sys


class QTDataTable(QTableWidget):
    def __init__(self, headers, data, only_column=None, parent=None):
        super().__init__(parent)
        self.all_headers = headers
        self.all_data = data
        self.only_column = only_column  # 只显示哪一列（字段名），如 "name"
        self.show_only = False  # 是否只显示 only_column

        self.refresh_table()

    def refresh_table(self):
        self.clear()
        if self.show_only and self.only_column in self.all_headers:
            self.setColumnCount(1)
            self.setRowCount(len(self.all_data))
            self.setHorizontalHeaderLabels([self.only_column])
            for row, row_data in enumerate(self.all_data):
                value = row_data.get(self.only_column, "")
                self.setItem(row, 0, QTableWidgetItem(str(value)))
        else:
            self.setColumnCount(len(self.all_headers))
            self.setRowCount(len(self.all_data))
            self.setHorizontalHeaderLabels(self.all_headers)
            for row, row_data in enumerate(self.all_data):
                for col, key in enumerate(self.all_headers):
                    value = row_data.get(key, "")
                    self.setItem(row, col, QTableWidgetItem(str(value)))

    def set_show_only(self, show_only: bool):
        self.show_only = show_only
        self.refresh_table()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTDataTable 示例")

        # 你的数据
        data = [
            {
                "id": "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}",
                "name": "Master Audio Bus",
            },
            {"id": "{0FB0256C-331C-4618-B069-1B1B33EA0E92}", "name": "SC_METER_EQ"},
            {"id": "{0FB0256C-331C-4618-B069-1B1B33EA0E92}", "name": "SC_METER_EQ"},
            {
                "id": "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}",
                "name": "Master Audio Bus",
            },
            {"id": "{CCFCAB8C-F878-416C-A3B1-1B88570D628E}", "name": "SC_METER_Meter"},
            {"id": "{CCFCAB8C-F878-416C-A3B1-1B88570D628E}", "name": "SC_METER_Meter"},
            {"id": "{CCFCAB8C-F878-416C-A3B1-1B88570D628E}", "name": "SC_METER_Meter"},
            {"id": "{0FB0256C-331C-4618-B069-1B1B33EA0E92}", "name": "SC_METER_EQ"},
            {
                "id": "{BDFF3B2A-0BFC-4A48-A696-8F0BD706CB0C}",
                "name": "Default Work Unit",
            },
            {
                "id": "{BDFF3B2A-0BFC-4A48-A696-8F0BD706CB0C}",
                "name": "Default Work Unit",
            },
        ]
        headers = ["name", "id"]

        self.table = QTDataTable(headers, data, only_column="name")

        self.btn_toggle = QPushButton("只显示 name")
        self.btn_toggle.setCheckable(True)
        self.btn_toggle.toggled.connect(self.on_toggle)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btn_toggle)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_toggle(self, checked):
        self.table.set_show_only(checked)
        self.btn_toggle.setText("显示全部" if checked else "只显示 name")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(700, 400)
    window.show()
    sys.exit(app.exec())
