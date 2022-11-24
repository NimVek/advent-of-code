import collections.abc
import enum
import math

import logging


__log__ = logging.getLogger(__name__)


class Vector(tuple):
    def __new__(cls, *args):
        if isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        return super().__new__(cls, args)

    def __add__(self, other):
        return Vector(map(sum, zip(self, other)))

    def norm(self, order):
        return sum(abs(i) ** order for i in self) ** (1.0 / order)

    def dot(self, other):
        return sum(math.prod(prod) for prod in zip(self, other))


class DirectionEnum(Vector, enum.Enum):
    pass


class Direction2D(DirectionEnum):
    NORTH = Vector(1, 0)
    SOUTH = Vector(-1, 0)
    EAST = Vector(0, 1)
    WEST = Vector(0, -1)
    N = NORTH
    S = SOUTH
    E = EAST
    W = WEST
    UP = NORTH
    DOWN = SOUTH
    RIGHT = EAST
    LEFT = WEST
    U = UP
    D = DOWN
    R = RIGHT
    L = LEFT
