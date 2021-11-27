import pytest
import solution_2015_12 as solution


@pytest.mark.parametrize(
    ("data", "result"),
    [
        ("[1,2,3]", 6),
        ('{"a":2, "b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4}, "c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
    ],
)
def test_one(data, result):
    assert solution.one(data) == result


@pytest.mark.parametrize(
    ("data", "result"),
    [
        ("[1,2,3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    ],
)
def test_two(data, result):
    assert solution.two(data) == result
