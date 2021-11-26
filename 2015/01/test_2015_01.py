import pytest
import solution_2015_01 as solution


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("(())", "0"),
        ("()()", "0"),
        ("(((", "3"),
        ("(()(()(", "3"),
        ("))(((((", "3"),
        ("())", "-1"),
        ("))(", "-1"),
        (")))", "-3"),
        (")())())", "-3"),
    ],
)
def test_one(input, output):
    assert str(solution.one(input)) == output


@pytest.mark.parametrize(
    ("input", "output"),
    [
        (")", "1"),
        ("()())", "5"),
    ],
)
def test_two(input, output):
    assert str(solution.two(input)) == output
