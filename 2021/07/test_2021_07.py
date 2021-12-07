import pytest
import solution_2021_07 as solution


@pytest.mark.parametrize(
    ("part", "output"),
    [
        ("one", 37),
        ("two", 168),
    ],
)
def test(part, output):
    x = ["16,1,2,0,4,2,7,1,2,14"]

    assert getattr(solution, part)("\n".join(x)) == output
