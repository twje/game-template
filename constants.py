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


class MessageID:
    GET_MAP = auto()
