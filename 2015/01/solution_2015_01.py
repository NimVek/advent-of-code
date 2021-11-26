def one(string):
    return string.count("(") - string.count(")")


def two(string):
    floor = 0
    for idx, val in enumerate(string):
        if val == "(":
            floor += 1
        if val == ")":
            floor -= 1
        if floor < 0:
            return idx + 1
