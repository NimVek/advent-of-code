import pytest
import solution_2015_15 as solution


@pytest.mark.parametrize(
    ("part", "value"),
    [
        ("one", 62842880),
        ("two", 57600000),
    ],
)
def test(part, value):
    ingredients = [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]
    assert getattr(solution, part)("\n".join(ingredients)) == value
