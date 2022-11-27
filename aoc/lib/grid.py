import enum

from .algebra import Matrix, Vector

import logging


__log__ = logging.getLogger(__name__)


class VectorEnum(Vector, enum.Enum):
    pass


Origin2D = Vector(0, 0)


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
