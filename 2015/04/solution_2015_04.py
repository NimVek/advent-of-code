import hashlib


def advent_coin(string, zeroes):
    idx = 0
    while (
        not hashlib.md5(f"{string}{idx}".encode()).hexdigest().startswith("0" * zeroes)
    ):
        idx += 1
    return idx


def one(string):
    return advent_coin(string, 5)


def two(string):
    return advent_coin(string, 6)
