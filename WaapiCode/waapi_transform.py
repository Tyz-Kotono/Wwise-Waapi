# === form ===

# Specify a list of object IDs (GUIDs). Used to find objects when you already have their IDs.

fromId: str = "id"

# Specify a set of object names qualified by type, in the form type:name. Only supports object types with globally unique names.

fromName: str = "name"

# Specify text to search in Wwise objects and comments. Uses the same search engine as in Wwise.

fromSearch: str = "search"

# Specify a list of absolute paths to find. Paths must start with the category name, like a physical folder name. Example: \Actor-Mixer Hierarchy\Default Work Unit\MySound.

fromPath: str = "path"

# Specify a list of Wwise object types. Used to get all objects of a certain type. Example: get all Game Parameters.

fromOfType: str = "ofType"

# === transform ===

# For each object, select the parent object.

selectParent: str = "parent"

# For each object, select the list of child objects.

selectChildren: str = "children"

# For each object, recursively select all descendant objects.

selectDescendants: str = "descendants"

# For each object, recursively select ancestor objects.

selectAncestors: str = "ancestors"

# For each object, select all objects that reference this object.

selectReferencesTo: str = "referencesTo"


# === Core Where ===

# Case-insensitive text search on the object name.

nameContains: str = "name:contains"

# Case-insensitive regular expression search on the object name.

nameMatches: str = "name:matches"

# Filter the previous iterator results, keeping only objects of specific types. See Wwise object reference for type list.

typeIsIn: str = "type:isIn"

# Filter the previous iterator results, keeping only objects of specific categories.

categoryIsIn: str = "category:isIn"

# Filter the previous iterator results, keeping only unique objects.

distinct: str = "distinct"

from .waapi_type import *
from .waapi_constants import *
from waapi import WaapiClient
from typing import List, Any, Dict


def Search_Object_By_Name(client: WaapiClient, text: str) -> list:
    """
    Search for objects in Wwise using a search string.
    :param client: WaapiClient instance
    :param text: Search string
    :return: List of objects matching the search string
    """
    args = {
        "from": {"search": [text]},
        "options": {"return": [Wwise_id, Wwise_type, Wwise_name]},
    }
    result = client.call(Wwise_core_object_get, args)

    if result and result["return"]:
        return result["return"]
    return []


def Serach_Object_By_Type(
    client: WaapiClient, name_substring: str, type_str: str
) -> list:
    args = {
        "from": {"ofType": [type_str]},
        "transform": [{"where": [nameContains, name_substring]}],
    }

    options = {"return": [Wwise_id, Wwise_type, Wwise_name]}

    result = client.call(Wwise_core_object_get, args, options=options)

    if result and result["return"]:
        return result["return"]
    return []
