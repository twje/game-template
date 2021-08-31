from enum import Enum
from enum import auto


class MapID(Enum):
    MAP_1 = auto()
    MAP_2 = auto()


class SceneID(Enum):
    GAME = auto()


class EntityStates:
    MOVE = "move"


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BUTTOM = auto()


MANIFEST_ID = "manifest"
ENTITY_DEF_ID = "entity_def"
ENTITY_DEF_FILEPATH = "entity_def.json"
