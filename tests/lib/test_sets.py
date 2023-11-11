import pytest

from aoc.lib.sets import Interval, IntervalSet


def test_interval_constructor():
    assert Interval(3, 4) == (3, 4)


@pytest.mark.parametrize(
    ("first", "second", "result"),
    [
        (Interval(3, 4), Interval(1, 5), Interval(3, 4)),
        (Interval(1, 5), Interval(3, 4), Interval(3, 4)),
        (Interval(1, 4), Interval(3, 5), Interval(3, 4)),
        (Interval(1, 3), Interval(4, 5), None),
    ],
)
def test_interval_intersection(first, second, result):
    assert first & second == result


def test_intervalset_union():
    assert IntervalSet([1, 10]) | IntervalSet([1, 4], [6, 10]) == IntervalSet([1, 10])
