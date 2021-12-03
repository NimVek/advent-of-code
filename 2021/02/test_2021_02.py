import pytest
import solution_2021_02 as solution


@pytest.mark.parametrize(
    ("part", "output"),
    [
        ("one", 150),
        ("two", 900),
    ],
)
def test(part, output):
    x = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    assert getattr(solution, part)("\n".join(x)) == output
