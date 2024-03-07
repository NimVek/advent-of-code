import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("string", "answer"),
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_nice_01(string, answer):

    assert Solution.nice_01(string) == answer  # nosec assert_used


@pytest.mark.parametrize(
    ("string", "answer"),
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_nice_02(string, answer):

    assert Solution.nice_02(string) == answer  # nosec assert_used
