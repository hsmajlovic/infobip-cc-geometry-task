from enum import Enum


class EventPointType(Enum):
    upper = 1
    intersection = 2
    bottom = 3


class SemiCircleSide(Enum):
    left = 1
    right = 2
