import pytest
import solution_2021_06 as solution


@pytest.mark.parametrize(
    ("part", "output"),
    [
        ("one", 5934),
        ("two", 26984457539),
    ],
)
def test(part, output):
    x = ["3,4,3,1,2"]

    assert getattr(solution, part)("\n".join(x)) == output
