#!/usr/bin/env python3

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from WaapiCode import *


from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

# https://www.audiokinetic.com/zh/public-library/2024.1.4_8780/?source=SDK&id=waapi_query.html

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:

        # # get parent of object by ID
        # args = {
        #     # 目標
        #     "from": {
        #         "id": [
        #             "{5C0F82B0-CB54-4103-9C6B-767B9CAA9E38}",
        #             "{4B2D62D4-B3E9-4E1A-AD64-6C6EF77E69F7}",
        #         ]
        #     },
        #     "transform": [
        #         # 選擇的對象
        #         {"select": ["parent"]},
        #         # condition
        #         {"where": ["name:contains", "e"]},
        #     ],
        # }

        # # 輸出什麼
        # options = (
        #     {"return": [Wwise_id, Wwise_type, Wwise_name, Wwise_path, Wwise_parent]},
        # )
        # result = client.call(Wwise_core_object_get, args, options)

        # pprint(result)

        args = {
            # 目標
            "from": {
                Wwise_id: [
                    "{5C0F82B0-CB54-4103-9C6B-767B9CAA9E38}",
                    "{4B2D62D4-B3E9-4E1A-AD64-6C6EF77E69F7}",
                ]
            },
            "transform": [
                # 選擇的對象
                {"select": [selectParent]},
                # condition
                {"where": [nameContains, "e"]},
            ],
        }

        options = (
            {"return": [Wwise_id, Wwise_type, Wwise_name, Wwise_path, Wwise_parent]},
        )
        result = client.call(Wwise_core_object_get, args, options)

        pprint(result)

except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
