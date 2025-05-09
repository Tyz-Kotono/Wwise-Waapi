from .waapi_type import *
from .waapi_constants import *
from waapi import WaapiClient
from typing import List, Any, Dict






def core_object_get_by_search(
    client: WaapiClient, search_string: str, options: list = None
) -> dict:
    if options is None:
        options = [Wwise_id, Wwise_type, Wwise_name]
    args = {
        "from": {"search": [search_string]},
        "options": {"return": options},
    }
    return client.call(Wwise_core_object_get, args)


def core_object_get_by_id(
    waapi: WaapiClient, object_id: str, options: List[Any] = None
) -> Dict:
    if options is None:
        options = [Wwise_id, Wwise_type, Wwise_name]
    args = {
        "from": {"id": [object_id]},
        "options": {"return": options},
    }
    return waapi.call(Wwise_core_object_get, args)
