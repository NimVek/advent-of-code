import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("part", "answer"),
    [
        (1, 7),
        (2, 5),
    ],
)
def test(part, answer):
    data = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]

    assert Solution.solve(part, data) == answer
