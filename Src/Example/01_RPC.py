import sys
import os

# 案例代码，所以不是项目根目录启动需要添加路径
# 这里是为了让PyCharm能找到QTUI和Core模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from QTUI import QTMainWindow
from WaapiCore import *

from waapi import CannotConnectToWaapiException
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PySide6.QtCore import Qt
import sys
from pprint import pprint

if __name__ == "__main__":


    with WaapiClient() as client:
        result = client.call(Wwise_core_getInfo)
        object_get_args = {
            "from": {"path": ["\\Actor-Mixer Hierarchy\\Default Work Unit"]},
            "options": {"return": ["id", "name", "type"]},
        }
        result = client.call("ak.wwise.core.object.get", object_get_args)
        pprint(result)
