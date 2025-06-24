using AK.WaapiNet.ObjectModel;

namespace AK.WaapiNet.ObjectModel
{
    /// <summary>
    /// Wwise对象分类系统
    /// </summary>
    public static class WwiseCategories
    {
        /// <summary>Actor-Mixer层级</summary>
        public const string ActorMixer = "Actor-Mixer Hierarchy";
        /// <summary>交互音乐层级</summary>
        public const string InteractiveMusic = "Interactive Music Hierarchy";
        /// <summary>事件系统</summary>
        public const string Events = "Events";
        /// <summary>主混音器层级</summary>
        public const string MasterMixer = "Master-Mixer Hierarchy";
        /// <summary>游戏同步器</summary>
        public const string GameSyncs = "Game Syncs";
        /// <summary>虚拟声学</summary>
        public const string VirtualAcoustics = "Virtual Acoustics";
        /// <summary>工程管理</summary>
        public const string Project = "Project";
    }

    /// <summary>
    /// Wwise对象类型系统
    /// </summary>
    
    /// <summary>
    /// Actor-Mixer类型
    /// </summary>
    public static class ActorMixerType
    {
        public const string Sound = "Sound";
        public const string RandomSequenceContainer = "RandomSequenceContainer";
        public const string BlendContainer = "BlendContainer";
        public const string SwitchContainer = "SwitchContainer";
        public const string AudioSource = "AudioSource";
        public const string ActorMixer = "ActorMixer";
    }

    /// <summary>
    /// 交互音乐类型
    /// </summary>
    public static class InteractiveMusicType
    {
        public const string MusicSegment = "MusicSegment";
        public const string MusicTrack = "MusicTrack";
        public const string MusicSwitchContainer = "MusicSwitchContainer";
    }

    /// <summary>
    /// 事件类型
    /// </summary>
    public static class EventsType
    {
        public const string Event = "Event";
        public const string Action = "Action";
    }

    /// <summary>
    /// 混音器类型
    /// </summary>
    public static class MixerType
    {
        public const string Bus = "Bus";
        public const string AuxBus = "AuxBus";
        public const string Effect = "Effect";
        public const string Attenuation = "Attenuation";
    }

    /// <summary>
    /// 游戏同步器类型
    /// </summary>
    public static class GameSyncsType
    {
        public const string GameParameter = "GameParameter";
        public const string StateGroup = "StateGroup";
        public const string State = "State";
        public const string SwitchGroup = "SwitchGroup";
        public const string Switch = "Switch";
    }

    /// <summary>
    /// 虚拟声学类型
    /// </summary>
    public static class VirtualAcousticsType
    {
        public const string AcousticTexture = "AcousticTexture";
    }

    /// <summary>
    /// 工程管理类型
    /// </summary>
    public static class ProjectType
    {
        public const string Folder = "Folder";
        public const string WorkUnit = "WorkUnit";
    }
    
    
    /// <summary>
    /// Wwise对象工具类
    /// </summary>
    public static class WwiseUtilities
    {
        /// <summary>
        /// 获取对象所属分类
        /// </summary>
        /// <param name="objectType">对象类型</param>
        /// <returns>分类名称</returns>

        public static string ActorMixer => @"\Actor-Mixer Hierarchy\Default Work Unit";
        public static string InteractiveMusic => @"\Interactive Music Hierarchy\Default Work Unit";
        public static string Events => @"\Events\Default Work Unit";
        public static string MasterMixer => @"\Master-Mixer Hierarchy\Default Work Unit";
        public static string GameSyncsGameParameter => @"\Game Parameters\Default Work Unit";
        public static string GameSyncsState => @"\States\Default Work Unit";
        public static string GameSyncs => @"\Switches\Default Work Unit";
        public static string VirtualAcoustics => @"\Virtual Acoustics\Default Work Unit";
    }
    
    
}