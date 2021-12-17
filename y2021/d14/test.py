import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("part", "output"),
    [
        (1, 1588),
        (2, 2188189693529),
    ],
)
def test(part, output):
    template = "NNCB"
    rules = [
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]

    assert Solution.solve(part, (template, rules)) == output
