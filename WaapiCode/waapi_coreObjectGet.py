from .waapi_type import *
from .waapi_constants import *


def setCoreObjectGet(waapi, searchString):
    args = {
        "from": {"search": [searchString]},
        "options": {"return": [Wwise_id, Wwise_type, Wwise_name]},
    }
    return waapi.call(Wwise_core_object_get, args)
