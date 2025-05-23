from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

"""
Documentation:
https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects.html
input:
https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects_options_schema.html
result:
https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects_result_schema.html

"""


def getSelectedObjects(client: WaapiClient, opstions: dir = None):

    if opstions is None:
        opstions = {"return": ["id", "type", "name"]}

    try:
        result = client.call("ak.wwise.ui.getSelectedObjects", options=opstions)
        return result["objects"]
    except Exception as e:
        return None


if __name__ == "__main__":
    with WaapiClient() as client:
        selected = getSelectedObjects(client)
        pprint(selected)
