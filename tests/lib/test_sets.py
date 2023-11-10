from aoc.lib.sets import Interval


class TestInterval:
    def test_constructor(self):
        assert Interval(3, 4) == (3, 4)

    def test_intersection(self):
        assert Interval(3, 4) & Interval(1, 5) == Interval(3, 4)
        assert Interval(1, 5) & Interval(3, 4) == Interval(3, 4)
        assert Interval(1, 4) & Interval(3, 5) == Interval(3, 4)
        assert Interval(1, 3) & Interval(4, 5) is None
