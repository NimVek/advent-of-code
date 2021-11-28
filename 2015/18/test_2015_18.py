import pytest
import solution_2015_18 as solution


@pytest.mark.parametrize(
    ("grid", "steps", "answer"),
    [
        (solution.Grid, 4, 4),
        (solution.StuckGrid, 5, 17),
    ],
)
def test(grid, steps, answer):
    lines = [
        ".#.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####..",
    ]
    assert solution.solution("\n".join(lines), grid, steps) == answer
