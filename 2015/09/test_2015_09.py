import pytest
import solution_2015_09 as solution


@pytest.mark.parametrize(
    ("part", "value"),
    [
        ("one", 605),
        ("two", 982),
    ],
)
def test(part, value):
    instructions = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    assert getattr(solution, part)("\n".join(instructions)) == value
