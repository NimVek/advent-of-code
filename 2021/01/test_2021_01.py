import pytest
import solution_2021_01 as solution


@pytest.mark.parametrize(
    ("part", "output"),
    [
        ("one", 7),
        ("two", 5),
    ],
)
def test(part, output):
    x = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]

    assert getattr(solution, part)("\n".join(x)) == output
