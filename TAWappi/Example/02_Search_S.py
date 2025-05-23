#!/usr/bin/env python3
import sys
import os

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_core_object_get.html


def Serach_Object_By_Type(
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


try:

    with WaapiClient() as client:
        result = Serach_Object_By_Type(client, "EQ", "Folder")
        pprint(result)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi")
