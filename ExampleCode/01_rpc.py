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
        result = client.call(Wwise_core_getInfo)

        object_get_args = {
            "from": {"path": ["\\Actor-Mixer Hierarchy\\Default Work Unit"]},
            "options": {"return": ["id", "name", "type"]},
        }
        result = client.call("ak.wwise.core.object.get", object_get_args)
        pprint(result)
except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
