import collections.abc
import enum
import math

import logging


__log__ = logging.getLogger(__name__)


class Vector(tuple):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        return super().__new__(cls, args)

    def __add__(self, other):
        return Vector(map(sum, zip(self, other)))

    def norm(self, order):
        return sum(abs(i) ** order for i in self) ** (1.0 / order)

    def dot(self, other):
        return sum(math.prod(prod) for prod in zip(self, other))


class VectorEnum(Vector, enum.Enum):
    pass


class Direction2D(VectorEnum):
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


class Matrix(tuple):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        return super().__new__(cls, args)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(*map(other.dot, self))
        return NotImplemented


class MatrixEnum(Matrix, enum.Enum):
    pass


class Rotation2D(MatrixEnum):
    CLOCKWISE = Matrix((0, -1), (1, 0))
    COUNTERCLOCKWISE = Matrix((0, 1), (-1, 0))
    CW = CLOCKWISE
    CCW = COUNTERCLOCKWISE
    RIGHT = CLOCKWISE
    LEFT = COUNTERCLOCKWISE
    R = RIGHT
    L = LEFT
