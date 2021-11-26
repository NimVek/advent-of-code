import pytest
import solution_2015_08 as solution


@pytest.mark.parametrize(
    ("part", "value"),
    [
        ("one", 12),
        ("two", 19),
    ],
)
def test(part, value):
    strings = [
        '""',
        '"abc"',
        '"aaa\\"aaa"',
        '"\\x27"',
    ]
    assert getattr(solution, part)("\n".join(strings)) == value
