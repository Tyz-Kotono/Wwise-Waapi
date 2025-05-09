#!/usr/bin/env python3
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from WaapiCode import *
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint


def Serach_Object_By_Type(
    client: WaapiClient, name_substring: str, type_str: str
) -> list:
    args = {
        "from": {"ofType": [type_str]},
        "transform": [{"where": [nameContains, name_substring]}],
    }

    options = {"return": [Wwise_id, Wwise_type, Wwise_name]}

    result = client.call(Wwise_core_object_get, args, options=options)

    if result and result["return"]:
        return result["return"]
    return []


try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        # result = Search_Object_By_Name(client, "EQ")
        # pprint(result)

        result = Serach_Object_By_Type(client, "EQ", "Folder")
        pprint(result)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi")
