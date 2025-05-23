import threading
from waapi import WaapiClient
from Core.SingletonMeta import SingletonMeta


class WaapiClientInstance(metaclass=SingletonMeta):
    def __init__(self):
        self._lock = threading.Lock()
        self._client = None

    def connect(self):
        with self._lock:
            if self._client is None:
                self._client = WaapiClient()

    def call(self, *args, **kwargs):
        with self._lock:
            if self._client is None:
                self.connect()
            return self._client.call(*args, **kwargs)

    def close(self):
        with self._lock:
            if self._client:
                self._client.close()
                self._client = None

    # https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects.html
    def call_Select(self):
        WwiseClient = WaapiClientInstance()
        result = WwiseClient.call(
            "ak.wwise.ui.getSelectedObjects",
            options={"return": ["id"]},
        )
        return result["objects"]
