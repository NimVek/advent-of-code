"""Tests for `aoc` package."""

import pytest

from aoc import main


@pytest.mark.parametrize(
    ("argument", "expected"),
    [
        ("--help", "show this help message and exit"),
        ("-h", "show this help message and exit"),
        ("--version", "aoc "),
    ],
)
def test_standard_arguments(capsys, argument, expected):
    with pytest.raises(SystemExit):
        main.main(args=[argument])
    captured = capsys.readouterr()
    assert expected in captured.out
