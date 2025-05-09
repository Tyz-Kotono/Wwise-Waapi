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

        # by string
        # _type = setCoreObjectGetBySearch(client, "EQ")
        # pprint(_type)

        # by ID
        # args = {
        #     "from": {"id": ["{5C0F82B0-CB54-4103-9C6B-767B9CAA9E38}"]},
        #     "options": {"return": [Wwise_id, Wwise_type, Wwise_name]},
        # }
        # result = client.call(Wwise_core_object_get, args)

        result = setCoreObjectGetByID(client, "{5C0F82B0-CB54-4103-9C6B-767B9CAA9E38}")
        pprint(result)


except CannotConnectToWaapiException:
    print(
        "Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?"
    )
