import pytest
import solution_2015_05 as solution


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("ugknbfddgicrmopn", "1"),
        ("aaa", "1"),
        ("jchzalrnumimnmhp", "0"),
        ("haegwjzuvuyypxyu", "0"),
        ("dvszwmarrgswjxmb", "0"),
    ],
)
def test_one(input, output):
    assert str(solution.one(input)) == output


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("qjhvhtzxzqqjkmpb", "1"),
        ("xxyxx", "1"),
        ("uurcxstgmygtbstg", "0"),
        ("ieodomkazucvgmuy", "0"),
    ],
)
def test_two(input, output):
    assert str(solution.two(input)) == output
