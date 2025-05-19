class WwiseDataSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.SelectList = []
            cls._instance.SearchList = []
        return cls._instance

    # 可选：添加操作方法
    def add_to_select(self, item):
        self.SelectList.append(item)

    def add_to_search(self, item):
        self.SearchList.append(item)

    def clear_select(self):
        self.SelectList.clear()

    def clear_search(self):
        self.SearchList.clear()
