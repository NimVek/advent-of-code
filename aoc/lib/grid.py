import enum

from .algebra import Matrix, Vector

import logging


__log__ = logging.getLogger(__name__)


Origin2D = Vector(0, 0)


class VectorEnum(Vector, enum.Enum):
    pass


class Direction2D(VectorEnum):
    NORTH = N = Vector(-1, 0)
    SOUTH = S = Vector(1, 0)
    EAST = E = Vector(0, 1)
    WEST = W = Vector(0, -1)
    UP = U = NORTH
    DOWN = D = SOUTH
    RIGHT = R = EAST
    LEFT = L = WEST


class MatrixEnum(Matrix, enum.Enum):
    pass


class Rotation2D(MatrixEnum):
    CLOCKWISE = CW = Matrix((0, 1), (-1, 0))
    COUNTERCLOCKWISE = CCW = Matrix((0, -1), (1, 0))
    RIGHT = R = CLOCKWISE
    LEFT = L = COUNTERCLOCKWISE
