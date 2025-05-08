# waapi_constants.py
"""
Wwise WAAPI Command Constants

This module defines WAAPI command strings as constants for easy reuse and typo prevention.
"""

# === Core Commands ===
WWISE_GET_INFO: str = "ak.wwise.core.getInfo"

# === Object Commands ===
WWISE_OBJECT_GET: str = "ak.wwise.core.object.get"
WWISE_OBJECT_SET_NAME: str = "ak.wwise.core.object.setName"
WWISE_OBJECT_CREATE: str = "ak.wwise.core.object.create"
WWISE_OBJECT_DELETE: str = "ak.wwise.core.object.delete"
WWISE_OBJECT_MOVE: str = "ak.wwise.core.object.move"

# === UI Commands ===
WWISE_UI_GET_SELECTED_OBJECTS: str = "ak.wwise.ui.getSelectedObjects"
WWISE_UI_BRING_TO_FRONT: str = "ak.wwise.ui.bringToFront"

# === Transport Commands ===
WWISE_TRANSPORT_CREATE: str = "ak.wwise.core.transport.create"
WWISE_TRANSPORT_DESTROY: str = "ak.wwise.core.transport.destroy"
WWISE_TRANSPORT_GET_STATE: str = "ak.wwise.core.transport.getState"
WWISE_TRANSPORT_PLAY: str = "ak.wwise.core.transport.play"
WWISE_TRANSPORT_STOP: str = "ak.wwise.core.transport.stop"
WWISE_TRANSPORT_PAUSE: str = "ak.wwise.core.transport.pause"

# === Example Paths ===
WWISE_PATH_DEFAULT_WORK_UNIT: str = r"\\Actor-Mixer Hierarchy\\Default Work Unit"

# === Default Return Fields ===
WWISE_RETURN_BASIC_INFO: list[str] = ["id", "name", "type"]
