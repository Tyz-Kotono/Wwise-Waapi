#!/usr/bin/env python3

import sys
import os
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

# https://www.audiokinetic.com/zh/public-library/2024.1.5_8803/?source=SDK&id=ak_wwise_ui_getselectedobjects.html


from Wwise_UI import *

if __name__ == "__main__":
    with WaapiClient() as client:
        selected = getSelectedObjects(client, opstions={"return": ["id", "name"]})
        pprint(selected)
