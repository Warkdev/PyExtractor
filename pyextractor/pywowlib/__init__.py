from .io_utils.types import singleton

@singleton
class WoWVersionManager:
    def __init__(self):
        self.client_version = 0

    def set_client_version(self, version: int):
        self.client_version = version

class WoWVersions:
    UNKNOWN = -1
    CLASSIC = 0
    TBC = 1
    WOTLK = 2
    CATA = 3
    MOP = 4
    WOD = 5  # ?
    LEGION = 6
    BFA = 7
    SHADOWLANDS = 8
    NEW_CLASSIC = 9
    NEW_TBC_CLASSIC = 10

    map_version_name = {
        UNKNOWN: 'Unknown',
        CLASSIC: 'Vanilla',
        TBC: 'The Burning Crusade',
        WOTLK: 'Wrath of the Lich King',
        CATA: 'Cataclysm',
        MOP: 'Mysts of Pandaria',
        WOD: 'Warolords of Draenor',
        LEGION: 'Legion',
        BFA: 'Battle for Azeroth',
        SHADOWLANDS: 'Shadowlands',
        NEW_CLASSIC: 'Classic Era',
        NEW_TBC_CLASSIC: 'The Burning Crusade Classic'
    }

    @staticmethod
    def get_version_name(version: int) -> str:
        return WoWVersions.map_version_name.get(version, 'Not supported: {}'.format(version))
