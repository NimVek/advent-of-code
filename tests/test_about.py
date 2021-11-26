import pytest

import aoc


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("title", "aoc"),
        (
            "summary",
            "Advent of Code Helper.",
        ),
        ("uri", "https://github.com/NimVek/advent-of-code/"),
        ("author", "NimVek"),
        ("email", "NimVek@users.noreply.github.com"),
        ("license", "GPL-3.0-or-later"),
    ],
)
def test_about(key, value):
    assert getattr(aoc, f"__{key}__") == value
