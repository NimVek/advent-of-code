import pytest
import solution_2015_11 as solution


@pytest.mark.parametrize(
    ("password", "result"),
    [
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
    ],
)
def test_check(password, result):
    assert solution.check(password) == result


@pytest.mark.parametrize(
    ("password", "result"),
    [
        ("xx", "xy"),
        ("xy", "xz"),
        ("xz", "ya"),
        ("ya", "yb"),
    ],
)
def test_increment(password, result):
    assert solution.increment(password) == result


@pytest.mark.parametrize(
    ("password", "result"),
    [
        ("abcdefgh", "abcdffaa"),
        ("ghijklmn", "ghjaabcc"),
    ],
)
def test_one(password, result):
    assert solution.one(password) == result
