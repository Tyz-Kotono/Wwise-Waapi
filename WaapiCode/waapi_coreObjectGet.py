from .waapi_type import *
from .waapi_constants import *


def setCoreObjectGetBySearch(
    waapi, searchString, options=[Wwise_id, Wwise_type, Wwise_name]
):
    args = {
        "from": {"search": [searchString]},
        "options": {"return": options},
    }
    return waapi.call(Wwise_core_object_get, args)


def setCoreObjectGetByID(
    waapi, searchString, options=[Wwise_id, Wwise_type, Wwise_name]
):
    args = {
        "from": {"id": [searchString]},
        "options": {"return": options},
    }
    return waapi.call(Wwise_core_object_get, args)
