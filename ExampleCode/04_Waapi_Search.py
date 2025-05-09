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

        _type = setCoreObjectGet(client, "EQ")

        # pprint(_type)

        pprint(_type)

except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
