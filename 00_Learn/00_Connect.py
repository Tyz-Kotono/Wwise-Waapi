from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    with WaapiClient() as client:
        
        # https://www.audiokinetic.com/zh/public-library/2024.1.4_8780/?source=SDK&id=ak_wwise_core_getinfo.html
        result = client.call("ak.wwise.core.getInfo")
        print("Connected Wwise!")
        # print(result)
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
