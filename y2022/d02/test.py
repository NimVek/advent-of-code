import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("strategy", "score"),
    [
        ("A Y", 8),
        ("B X", 1),
        ("C Z", 6),
    ],
)
def test_strategy_response(strategy, score):
    assert Solution.strategy_response(strategy) == score


@pytest.mark.parametrize(
    ("strategy", "score"),
    [
        ("A Y", 4),
        ("B X", 1),
        ("C Z", 7),
    ],
)
def test_strategy_outcome(strategy, score):
    assert Solution.strategy_outcome(strategy) == score
