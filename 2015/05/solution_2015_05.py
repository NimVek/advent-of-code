import re


def one(string):
    result = 0
    for word in string.splitlines():
        if (
            (len(re.findall(r"[aeiou]", word)) > 2)
            and re.search(r"(.)\1", word)
            and not re.search(r"(ab|cd|pq|xy)", word)
        ):
            result += 1
    return result


def two(string):
    result = 0
    for word in string.splitlines():
        if re.search(r"(..).*\1", word) and re.search(r"(.).\1", word):
            result += 1
    return result
