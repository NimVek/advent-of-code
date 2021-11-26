import pytest
import solution_2015_04 as solution


@pytest.mark.slow
@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("abcdef", "609043"),
        ("pqrstuv", "1048970"),
    ],
)
def test_one(input, output):
    assert str(solution.one(input)) == output


@pytest.mark.slow
@pytest.mark.parametrize(
    ("input", "output"),
    [],
)
def test_two(input, output):
    assert str(solution.two(input)) == output
