#!/usr/bin/env python3
import sys
import os


from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=waapi_client_python_rpc.html
# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_core_getinfo.html


try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        result = client.call("ak.wwise.core.getInfo")

        version_string = result["version"]["displayName"]

        pprint(version_string)
except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
