#!/usr/bin/env python3

import sys
import os
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint


# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects.html


try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:

        result = client.call(
            "ak.wwise.ui.getSelectedObjects",
            options={"return": ["id", "type", "name"]},
        )

        _type = result["objects"]  # [0]["type"]
        # version_string = result["version"][DISPLAY_NAME]

        pprint(_type)

        for i in result["objects"]:
            if i["type"] == "Sound":
                print(f"Sound: {i['name']}")
            elif i["type"] == "Event":
                print(f"Event: {i['name']}")
            elif i["type"] == "SwitchGroup":
                print(f"SwitchGroup: {i['name']}")
            else:
                print(f"Unknown type: {i['name']}")

except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
