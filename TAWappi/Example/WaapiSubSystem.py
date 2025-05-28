from pprint import pprint
import threading
from enum import Enum, auto
from waapi import WaapiClient, CannotConnectToWaapiException


class WwiseListType(Enum):
    SELECT = auto()
    SEARCH = auto()
    FROM = auto()
    OPTIONS = auto()
    RETURN = auto()


class SingletonMeta(type):
    """
    线程安全的单例元类
    """

    _instances = {}
    _lock = threading.Lock()  # 用于线程同步

    def __call__(cls, *args, **kwargs):
        # 双重检查锁定（Double-checked locking）
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


# 这个类用于管理 Wwise 数据实例，确保只有一个实例存在
# 通过 SingletonMeta 元类实现单例模式


class WwiseDataInstance(metaclass=SingletonMeta):
    def __init__(self):
        self.WwiseClinet = WaapiClient()
        self.searchID = []
        self.selectID = []
        # 用字典统一管理所有列表
        self.options_List = {}
        self.Data_lists = {}

    def getClient(self):
        """获取 Wwise 客户端实例"""
        if self.WwiseClinet is None:
            raise CannotConnectToWaapiException("Wwise 客户端未初始化")
        return self.WwiseClinet

    def GetClinetAndOptions(self, type: WwiseListType):
        """获取 Wwise 客户端和选项列表"""
        if self.WwiseClinet is None:
            raise CannotConnectToWaapiException("Wwise 客户端未初始化")
        return self.WwiseClinet, self.get_optionsList(WwiseListType.SELECT)

    def get_id(self, type: WwiseListType):
        if type == WwiseListType.SELECT:
            return self.selectID
        elif type == WwiseListType.SEARCH:
            return self.searchID

    def set_id(self, ids, type: WwiseListType):
        if type == WwiseListType.SELECT:
            self.selectID = list({id["id"] for id in ids})
        elif type == WwiseListType.SEARCH:
            self.searchID = list({id["id"] for id in ids})

    def set_Datalist(self, list_type: WwiseListType, lists=None):
        self.Data_lists[list_type] = lists

    def get_Datalist(self, list_type: WwiseListType):
        # 如果不存在则自动创建一个空列表
        if list_type not in self.Data_lists:
            self.Data_lists[list_type] = []
        return self.Data_lists[list_type]

    def Set_optionsList(self, list_type: WwiseListType, options=None):
        self.options_List[list_type] = options

    def get_optionsList(self, list_type: WwiseListType):
        # 如果不存在则自动创建一个空列表
        if list_type not in self.options_List:
            self.options_List[list_type] = []
        return self.options_List[list_type]

    def refresh_list(self, list_type: WwiseListType, items):
        if not isinstance(items, (list, tuple, set)):
            items = [items]
        # 自动创建并替换
        self._lists[list_type] = list(items)

    # 可选：如果你想获取所有类型的列表
    def all_lists(self):
        return self._lists

    def CloseClient(self):
        """关闭 Wwise 客户端连接"""
        if self.WwiseClinet:
            try:
                self.WwiseClinet.disconnect()
                print("关闭事件触发")
            except CannotConnectToWaapiException as e:
                print(f"无法关闭 Wwise 客户端: {e}")
            finally:
                self.WwiseClinet = None
