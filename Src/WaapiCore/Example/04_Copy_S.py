#!/usr/bin/env python3
import sys
import os

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint


def Search_Object_By_Type(
    client: WaapiClient, name_substring: str, type_str: str
) -> list:
    args = {
        "from": {"ofType": [type_str]},
        "transform": [{"where": ["name:contains", name_substring]}],
    }

    options = {"return": ["id", "type", "name"]}

    result = client.call("ak.wwise.core.object.get", args, options=options)

    if result and result["return"]:
        return result["return"]
    return []


# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_core_object_copy.html
def waapi_copy(client: WaapiClient, _object: str, parent_id: str, new_name: str = None):
    args = {"object": _object, "parent": parent_id, "onNameConflict": "rename"}
    if new_name:
        args["name"] = new_name

    result = client.call("ak.wwise.core.object.copy", args)
    return result


if __name__ == "__main__":
    try:
        with WaapiClient() as client:
            # 先搜索符合条件的对象
            parent = Search_Object_By_Type(client, "Test", "Folder")
            result = Search_Object_By_Type(client, "copy", "ActorMixer")
            # pprint(parent)
            # pprint(result)
            parent_id = parent[0]["id"]
            result_id = result[0]["id"]
            # 你需要指定复制到哪个父对象下，这里举例用一个父对象ID
            pprint(parent_id)
            pprint(result_id)

            copy_result = waapi_copy(client, result_id, parent_id)
            pprint(copy_result)

    except CannotConnectToWaapiException:
        print("Could not connect to Waapi")
