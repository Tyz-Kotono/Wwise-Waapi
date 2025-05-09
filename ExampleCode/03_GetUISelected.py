#!/usr/bin/env python3

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from WaapiCode import *

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint


try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:

        result = client.call(
            Wwise_ui_getSelectedObjects,
            options={"return": [Wwise_id, Wwise_type, Wwise_name]},
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
