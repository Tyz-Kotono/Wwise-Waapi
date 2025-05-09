# https://www.audiokinetic.com/zh/public-library/2024.1.4_8780/?source=SDK&id=ak_wwise_core_getinfo.html

# Wwise session ID.

Wwise_sessionId: str = "sessionId"

# Object GUID in the form: {aabbcc00-1122-3344-5566-77889900aabb}.

Wwise_guid: str = "guid"

# Wwise Authoring API version. Range: [1,*]

Wwise_apiVersion: str = "apiVersion"

# Wwise display name.

Wwise_displayName: str = "displayName"

# Build branch.

Wwise_branch: str = "branch"

# Copyright info.

Wwise_copyright: str = "copyright"

# Wwise version object.

Wwise_version: str = "version"

# Wwise version name.

Wwise_version_displayName: str = "version.displayName"

# Version year. Range: [2000,2100]

Wwise_version_year: str = "version.year"

# Major version. Range: [0,100]

Wwise_version_major: str = "version.major"

# Minor version. Range: [0,100]

Wwise_version_minor: str = "version.minor"

# Build number. Range: [1,*]

Wwise_version_build: str = "version.build"

# Special name for a version.

Wwise_version_nickname: str = "version.nickname"

# Wwise project and Work Unit schema version. Range: [1,*]

Wwise_version_schema: str = "version.schema"

# Indicates Release or Debug build. Possible values: release, debug

Wwise_configuration: str = "configuration"

# Indicates Wwise build platform. Possible values: x64, win32, macosx, linux

Wwise_platform: str = "platform"

# Indicates if Wwise is running in command line.

Wwise_isCommandLine: str = "isCommandLine"

# Wwise process identifier.

Wwise_processId: str = "processId"

# Wwise process path.

Wwise_processPath: str = "processPath"

# Wwise directories object.

Wwise_directories: str = "directories"

# Wwise root directory. This is the install directory.

Wwise_directories_install: str = "directories.install"

# Wwise authoring root directory.

Wwise_directories_authoring: str = "directories.authoring"

# Bin directory containing Wwise.exe.

Wwise_directories_bin: str = "directories.bin"

# Help directory.

Wwise_directories_help: str = "directories.help"

# Wwise user data root directory.

Wwise_directories_user: str = "directories.user"
