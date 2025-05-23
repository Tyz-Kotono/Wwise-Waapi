{
    "type": "object",
    "properties": {
        "object": {
            "anyOf": [
                {
                    "type": "string",
                    "pattern": "^(StateGroup|SwitchGroup|SoundBank|GameParameter|Event|Effect|AudioDevice|Trigger|Attenuation|DialogueEvent|Bus|AuxBus|Conversion|ModulatorLfo|ModulatorEnvelope|ModulatorTime|Platform|Language|AcousticTexture|Global):[a-zA-Z0-9_]+$",
                    "description": "由类型或 Short ID 限定的对象名称，格式为 type:name 或 Global:shortId。仅支持采用全局唯一名称或 Short Id 的对象类型。例如：Event:Play_Sound_01, Global:245489792",
                },
                {
                    "type": "string",
                    "pattern": "^\\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\\}$",
                    "description": "以下形式的对象 GUID：{aabbcc00-1122-3344-5566-77889900aabb}。",
                },
                {
                    "type": "string",
                    "pattern": "^\\\\",
                    "description": "Wwise 对象的工程路径，包含类别和 Work Unit。例如：\\\\Actor-Mixer Hierarchy\\\\Default Work Unit\\\\New Sound SFX。",
                },
            ],
            "description": "所要复制的对象的 ID (GUID)、名称或路径。",
        },
        "parent": {
            "anyOf": [
                {
                    "type": "string",
                    "pattern": "^(StateGroup|SwitchGroup|SoundBank|GameParameter|Event|Effect|AudioDevice|Trigger|Attenuation|DialogueEvent|Bus|AuxBus|Conversion|ModulatorLfo|ModulatorEnvelope|ModulatorTime|Platform|Language|AcousticTexture|Global):[a-zA-Z0-9_]+$",
                    "description": "由类型或 Short ID 限定的对象名称，格式为 type:name 或 Global:shortId。仅支持采用全局唯一名称或 Short Id 的对象类型。例如：Event:Play_Sound_01, Global:245489792",
                },
                {
                    "type": "string",
                    "pattern": "^\\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\\}$",
                    "description": "以下形式的对象 GUID：{aabbcc00-1122-3344-5566-77889900aabb}。",
                },
                {
                    "type": "string",
                    "pattern": "^\\\\",
                    "description": "Wwise 对象的工程路径，包含类别和 Work Unit。例如：\\\\Actor-Mixer Hierarchy\\\\Default Work Unit\\\\New Sound SFX。",
                },
            ],
            "description": "对象的新父对象的 ID (GUID)、名称或路径。",
        },
        "onNameConflict": {
            "type": "string",
            "description": '在 "parent" 已经包含同名子对象时所要执行的操作。默认值为 "fail"。',
            "enum": ["rename", "replace", "fail"],
        },
        "autoCheckOutToSourceControl": {
            "type": "boolean",
            "description": "Determines if Wwise automatically performs a Checkout source control operation for affected work units and for the project. 默认设为 true。",
        },
        "autoAddToSourceControl": {
            "type": "boolean",
            "description": "Determines if Wwise automatically performs an Add source control operation for affected work units. 默认设为 true。",
        },
    },
    "required": ["object", "parent"],
    "additionalProperties": false,
}
