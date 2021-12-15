import pytest

from . import solution


@pytest.mark.parametrize(
    ("part", "output"),
    [
        ("one", 1588),
        ("two", 2188189693529),
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

    assert getattr(solution, part)((template, rules)) == output
