import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("data", "output"),
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part_one(data, output):
    assert Solution.solve(1, data) == output  # nosec assert_used


@pytest.mark.parametrize(
    ("data", "output"),
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_part_two(data, output):
    assert Solution.solve(2, data) == output  # nosec assert_used
