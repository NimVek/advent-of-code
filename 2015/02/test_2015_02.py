import pytest
import solution_2015_02 as solution


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("2x3x4", "58"),
        ("1x1x10", "43"),
    ],
)
def test_one(input, output):
    assert str(solution.one(input)) == output


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("2x3x4", "34"),
        ("1x1x10", "14"),
    ],
)
def test_two(input, output):
    assert str(solution.two(input)) == output
