import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("part", "answer"),
    [
        (1, 739785),
        (2, 444356092776315),
    ],
)
def test(part, answer):
    data = ["Player 1 starting position: 4", "Player 2 starting position: 8"]
    assert Solution.solve(part, data) == answer
