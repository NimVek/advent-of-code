import pytest
import solution_2016_01 as solution


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ],
)
def test_one(input, output):
    assert solution.one(input) == output


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("R8, R4, R4, R8", 4),
    ],
)
def test_two(input, output):
    assert solution.two(input) == output
