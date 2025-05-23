#!/usr/bin/env python3
import sys
import os


from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint


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
