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

    options = {"return": ["id", "type", "name", "parent"]}

    result = client.call("ak.wwise.core.object.get", args, options=options)

    if result and result["return"]:
        return result["return"]
    return []


# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_core_object_copy.html
def waapi_copy(client: WaapiClient, _object: str, parent_id: str, new_name: str = None):
    args = {
        "object": _object,
        "parent": parent_id,
        "onNameConflict": "rename",  # 默认是自动重命名
    }

    # 如果 new_name 存在，复制后你可以再次通过 API 修改名称
    result = client.call("ak.wwise.core.object.copy", args)

    # 如果指定了新的名字，修改复制后的对象名称
    if result and new_name:
        copied_object_id = result["return"]["id"]
        name_change_args = {
            "object": copied_object_id,
            "name": new_name,
        }
        # 修改对象的名称
        client.call("ak.wwise.core.object.setName", name_change_args)

    return result


if __name__ == "__main__":
    try:
        with WaapiClient() as client:
            # 先搜索符合条件的对象
            result = Search_Object_By_Type(client, "CopyTest_1", "Folder")

            # pprint(parent)
            # pprint(result)
            parent_id = result[0]["parent"]["id"]
            result_id = result[0]["id"]
            # 你需要指定复制到哪个父对象下，这里举例用一个父对象ID
            pprint(parent_id)
            pprint(result_id)

            newName = result[0]["name"] + "_copy"
            newName = result[0]["name"] + "_copy"
            copy_result = waapi_copy(client, result_id, parent_id, newName)
            pprint(copy_result)

    except CannotConnectToWaapiException:
        print("Could not connect to Waapi")
