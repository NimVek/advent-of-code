import pytest
import solution_2015_14 as solution


@pytest.mark.parametrize(
    ("speed", "fly", "rest", "time", "distance"),
    [
        (14, 10, 127, 1000, 1120),
        (16, 11, 162, 1000, 1056),
    ],
)
def test_reindeer(speed, fly, rest, time, distance):
    assert solution.Reindeer(speed, fly, rest).distance(time) == distance
