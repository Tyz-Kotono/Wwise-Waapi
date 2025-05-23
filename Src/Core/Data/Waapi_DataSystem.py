from Core.SingletonMeta import SingletonMeta
from pprint import pprint
from WaapiCore import WwiseListType


class WwiseDataSystem(metaclass=SingletonMeta):
    def __init__(self):
        self.searchID = []
        self.selectID = []
        # 用字典统一管理所有列表
        self._lists = {}

    def get_id(self, type: WwiseListType):
        if type == WwiseListType.SELECT:
            return self.selectID
        elif type == WwiseListType.SEARCH:
            return self.searchID

    def set_id(self, ids, type: WwiseListType):
        pprint(ids)
        # 直接用列表推导式提取 id，假设每个元素都是字典且包含 "id" 键
        # 如果你确定每个字典都有 "id"，可以直接写
        if type == WwiseListType.SELECT:
            self.selectID = list({id["id"] for id in ids})
        elif type == WwiseListType.SEARCH:
            self.searchID = list({id["id"] for id in ids})

    def get_list(self, list_type: WwiseListType):
        # 如果不存在则自动创建一个空列表
        if list_type not in self._lists:
            self._lists[list_type] = []
        return self._lists[list_type]

    def refresh_list(self, list_type: WwiseListType, items):
        if not isinstance(items, (list, tuple, set)):
            items = [items]
        # 自动创建并替换
        self._lists[list_type] = list(items)

    # 可选：如果你想获取所有类型的列表
    def all_lists(self):
        return self._lists


# 用法示例
if __name__ == "__main__":
    ds = WwiseDataSystem()
    ds.refresh_list(WwiseListType.SELECT, [1, 2, 3])
    print(ds.get_list(WwiseListType.SELECT))  # [1, 2, 3]
    print(ds.get_list(WwiseListType.SEARCH))  # []
