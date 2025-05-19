"""
Wwise WAAPI Command Constants

This module defines WAAPI command strings as constants for easy reuse and typo prevention.
"""

# === Core Commands ===
# https://www.audiokinetic.com/zh/public-library/2024.1.4_8780/?source=SDK&id=ak_wwise_core_getinfo.html

Wwise_core_getInfo: str = "ak.wwise.core.getInfo"


# === Object Commands ===
# https://www.audiokinetic.com/zh/public-library/2024.1.4_8780/?source=SDK&id=ak_wwise_core_object_get.html

Wwise_core_object_get: str = "ak.wwise.core.object.get"
Wwise_core_object_setName: str = "ak.wwise.core.object.setName"
Wwise_core_object_create: str = "ak.wwise.core.object.create"
Wwise_core_object_delete: str = "ak.wwise.core.object.delete"
Wwise_core_object_move: str = "ak.wwise.core.object.move"

# === UI Commands ===
Wwise_ui_getSelectedObjects: str = "ak.wwise.ui.getSelectedObjects"
Wwise_ui_bringToFront: str = "ak.wwise.ui.bringToFront"

# === Transport Commands ===
Wwise_core_transport_create: str = "ak.wwise.core.transport.create"
Wwise_core_transport_destroy: str = "ak.wwise.core.transport.destroy"
Wwise_core_transport_getState: str = "ak.wwise.core.transport.getState"
Wwise_core_transport_play: str = "ak.wwise.core.transport.play"
Wwise_core_transport_stop: str = "ak.wwise.core.transport.stop"
Wwise_core_transport_pause: str = "ak.wwise.core.transport.pause"

# === Example Paths ===
Wwise_path_defaultWorkUnit: str = r"\\Actor-Mixer Hierarchy\\Default Work Unit"

# === Default Return Fields ===
Wwise_return_basicInfo: list[str] = ["id", "name", "type"]
