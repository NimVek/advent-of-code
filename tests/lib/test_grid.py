import pytest

from aoc.lib.grid import Direction2D, Rotation2D


@pytest.mark.parametrize(
    ("direction", "rotation", "result"),
    [
        (Direction2D.NORTH, Rotation2D.CLOCKWISE, Direction2D.EAST),
        (Direction2D.EAST, Rotation2D.CLOCKWISE, Direction2D.SOUTH),
        (Direction2D.SOUTH, Rotation2D.CLOCKWISE, Direction2D.WEST),
        (Direction2D.WEST, Rotation2D.CLOCKWISE, Direction2D.NORTH),
        (Direction2D.NORTH, Rotation2D.COUNTERCLOCKWISE, Direction2D.WEST),
        (Direction2D.WEST, Rotation2D.COUNTERCLOCKWISE, Direction2D.SOUTH),
        (Direction2D.SOUTH, Rotation2D.COUNTERCLOCKWISE, Direction2D.EAST),
        (Direction2D.EAST, Rotation2D.COUNTERCLOCKWISE, Direction2D.NORTH),
    ],
)
def test_rotation(direction, rotation, result):
    assert rotation * direction == result
