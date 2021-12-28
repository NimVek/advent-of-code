import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("part", "answer"),
    [
        (1, None),
        (2, None),
    ],
)
def test(part, answer):
    data = None

    assert Solution.solve(part, data) == answer
