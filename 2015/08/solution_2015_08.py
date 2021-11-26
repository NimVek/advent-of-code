def one(string):
    result = 0
    for line in string.splitlines():
        result += len(line) - len(eval(line))
    return result


def two(string):
    result = 0
    for line in string.splitlines():
        result += (
            2 + len(line.translate({i: "\\" + chr(i) for i in b"\"\\'"})) - len(line)
        )
    return result
