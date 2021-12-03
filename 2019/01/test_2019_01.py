import pytest
import solution_2019_01 as solution


@pytest.mark.parametrize(
    ("mass", "fuel"),
    [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ],
)
def test_fuel(mass, fuel):
    assert solution.fuel(mass) == fuel


@pytest.mark.parametrize(
    ("mass", "fuel"),
    [
        (14, 2),
        (1969, 966),
        (100756, 50346),
    ],
)
def test_fuelfuel(mass, fuel):
    assert solution.fuelfuel(mass) == fuel
