import pytest
import solution_2015_10 as solution


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
def test_look_and_say(sequence, result):
    assert solution.look_and_say("1") == "11"
