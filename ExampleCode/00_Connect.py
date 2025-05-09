from pprint import pprint
from waapi import WaapiClient, CannotConnectToWaapiException

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from WaapiCode import *

try:
    with WaapiClient() as client:

        result = client.call(Wwise_core_getInfo)
        print("Connected Wwise!")
        # print(result)
except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
