import re


def check(string):
    result = False
    for i in range(0, len(string) - 2):
        k = 0
        for j in range(1, 3):
            if ord(string[i + j]) - ord(string[i]) == j:
                k += 1
        if k == 2:
            result = True
    if re.search(r"[iol]", string):
        result = False
    if len(re.findall(r"(\w)\1", string)) < 2:
        result = False
    return result


def increment(string):
    m = re.search(r"z*$", string)
    idx = m.start()
    result = (
        string[: idx - 1] + chr(ord(string[idx - 1]) + 1) + "a" * (len(string) - idx)
    )
    m = re.search(r"[iol].*$", result)
    if m:
        idx = m.start() + 1
        result = (
            string[: idx - 1]
            + chr(ord(string[idx - 1]) + 1)
            + "a" * (len(string) - idx)
        )
    return result


def one(string):
    string = increment(string)
    while not check(string):
        string = increment(string)
    return string


def two(string):
    return one(one(string))
