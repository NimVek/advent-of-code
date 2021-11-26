def one(string):
    result = 0
    for present in string.splitlines():
        sides = [int(x) for x in present.split("x")]
        sides.sort()
        result += (
            3 * sides[0] * sides[1] + 2 * sides[0] * sides[2] + 2 * sides[1] * sides[2]
        )
    return result


def two(string):
    result = 0
    for present in string.splitlines():
        sides = [int(x) for x in present.split("x")]
        sides.sort()
        result += 2 * sides[0] + 2 * sides[1] + sides[0] * sides[1] * sides[2]
    return result
