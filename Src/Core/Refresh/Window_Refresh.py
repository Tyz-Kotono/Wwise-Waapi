from Core import *
from pprint import pprint
from Core.SingletonMeta import SingletonMeta
from Core.Wwise.WaapiClientSystem import WaapiClientInstance
from Core.Data.Waapi_DataSystem import WwiseDataSystem
from WaapiCore import WwiseListType


class WindowRefreshSystem(metaclass=SingletonMeta):
    def Update(self, event=None):
        UpdateDataSelectedID()


def UpdateDataSelectedID():
    result = WaapiClientInstance().call_Select()
    WwiseDataSystem().set_id(result, WwiseListType.SELECT)
