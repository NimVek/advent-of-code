import pytest
import solution_2015_03 as solution


@pytest.mark.parametrize(
    ("input", "output"),
    [
        (">", "2"),
        ("^>v<", "4"),
        ("^v^v^v^v^v", "2"),
    ],
)
def test_one(input, output):
    assert str(solution.one(input)) == output


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("^v", "3"),
        ("^>v<", "3"),
        ("^v^v^v^v^v", "11"),
    ],
)
def test_two(input, output):
    assert str(solution.two(input)) == output
