#!/usr/bin/env python3
import sys
import os
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from WaapiCode import * 



try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        # NOTE: client will automatically disconnect at the end of the scope

        # == Simple RPC without argument
        # print("Getting Wwise instance information:")

        # https://www.audiokinetic.com/zh/public-library/2024.1.4_8780/?source=SDK&id=ak_wwise_core_getinfo.html

        result = client.call(WWISE_GET_INFO)

        version_string = result['version'][DISPLAY_NAME]
        
      
        
        pprint(version_string)
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
