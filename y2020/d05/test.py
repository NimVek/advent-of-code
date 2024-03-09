import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("seat", "seat_id"),
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test(seat, seat_id):
    assert Solution.seat_id(seat) == seat_id  # nosec assert_used
