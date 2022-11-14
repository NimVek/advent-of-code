import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("passphrase", "answer"),
    [
        (("aa", "bb", "cc", "dd", "ee"), True),
        (("aa", "bb", "cc", "dd", "aa"), False),
        (("aa", "bb", "cc", "dd", "aaa"), True),
    ],
)
def test_valid01(passphrase, answer):
    assert Solution.valid_01(passphrase) == answer


@pytest.mark.parametrize(
    ("passphrase", "answer"),
    [
        (("abcde", "fghij"), True),
        (("abcde", "xyz", "ecdab"), False),
        (("a", "ab", "abc", "abd", "abf", "abj"), True),
        (("iiii", "oiii", "ooii", "oooi", "oooo"), True),
        (("oiii", "ioii", "iioi", "iiio"), False),
    ],
)
def test_valid02(passphrase, answer):
    assert Solution.valid_02(passphrase) == answer
