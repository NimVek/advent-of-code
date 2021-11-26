import functools
import re


def look_and_say(string):
    result = ""
    for i in re.findall(r"((\d)\2*)", string):
        result += f"{len(i[0])}{i[1]}"
    return result


def solution(string, times):
    for i in range(0, times):
        string = look_and_say(string)
    return len(string)


one = functools.partial(solution, times=40)
two = functools.partial(solution, times=50)
