import threading


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


class TESTWindowRefreshSystem(metaclass=SingletonMeta):
    def __init__(self):
        # 初始化代码
        print("WindowRefreshSystem 初始化")

    def refresh(self):
        print("刷新窗口")


# 测试多线程环境下的单例
def task():
    instance = TESTWindowRefreshSystem()
    print(f"实例ID: {id(instance)}")


if __name__ == "__main__":
    threads = []
    for _ in range(5):
        t = threading.Thread(target=task)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
