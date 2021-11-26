def one(string):
    location = [0, 0]
    houses = set([tuple(location)])
    for direction in string:
        if direction == "^":
            location[0] += 1
        elif direction == "v":
            location[0] -= 1
        elif direction == ">":
            location[1] += 1
        elif direction == "<":
            location[1] -= 1
        houses.add(tuple(location))
    return len(houses)


def two(string):
    location = [[0, 0], [0, 0]]
    houses = set([tuple(location[0])])
    idx = 0
    for direction in string:
        if direction == "^":
            location[idx][0] += 1
        elif direction == "v":
            location[idx][0] -= 1
        elif direction == ">":
            location[idx][1] += 1
        elif direction == "<":
            location[idx][1] -= 1
        houses.add(tuple(location[idx]))
        idx = (idx + 1) % 2
    return len(houses)
