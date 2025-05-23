from Core import *
from WaapiCore import *
from QTUI import *

from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtCore import QEvent as QEventType
import sys


def BeginConnect():
    WwiseClient = WaapiClientInstance()
    WwiseClient.connect()
    QTWindow.AddCallBackEvent(
        QEventType.Type.Enter,
        [
            # lambda: WwiseDataSystem().Update(QTWindow),
            lambda: WindowRefreshSystem().Update(),
        ],
    )

    QTWindow.AddCallBackEvent(QEventType.Type.Leave, [lambda: print("Leave")])
    # QTWindow.AddCallBackEvent(
    #     QEventType.Type.Close,
    #     [lambda: WaapiClientManager().close(), lambda: print("Close Window")],
    # )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    QTWindow = QTMainWindow("Wwise Tool")
    QTWindow.resize(300, 200)
    QTWindow.show()
    BeginConnect()
    sys.exit(app.exec())
