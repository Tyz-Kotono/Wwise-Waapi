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


# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_core_object_setname.html


def waapi_rename(client: WaapiClient, _object: str, _newName: str):
    arg = {"object": _object, "value": _newName}
    client.call("ak.wwise.core.object.setName", arg)


if __name__ == "__main__":
    try:
        with WaapiClient() as client:
            # 先搜索符合条件的对象
            objects_to_copy = Search_Object_By_Type(client, "CopyTest_11", "Folder")
            pprint(objects_to_copy)
            parent_id = objects_to_copy[0]["id"]
            # 你需要指定复制到哪个父对象下，这里举例用一个父对象ID
            pprint(parent_id)

            waapi_rename(client, parent_id, "CopyTest_22")
            # objects_to_copy = Search_Object_By_Type(client, "EQ", "Folder")

            # pprint(objects_to_copy)

    except CannotConnectToWaapiException:
        print("Could not connect to Waapi")
