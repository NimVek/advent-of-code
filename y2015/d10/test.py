import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("sequence", "result"),
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
    ],
)
def test(sequence, result):
    assert Solution.look_and_say(sequence) == result  # nosec assert_used
