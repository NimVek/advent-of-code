import re

class Grid:
    def __init__(self):
       self.width = 1000
       self.height = 1000
       self.lights = [0] * self.width * self.height

    def brightness(self):
       return sum(self.lights)

class GridOne(Grid):
    def on(self, x, y):
       self.lights[ y * self.width + x ] = 1

    def off(self, x, y):
       self.lights[ y * self.width + x ] = 0

    def toggle(self, x, y):
       self.lights[ y * self.width + x ] = (self.lights[ y * self.width + x ] + 1) %2

class GridTwo(Grid):
    def on(self, x, y):
       self.lights[ y * self.width + x ] += 1

    def off(self, x, y):
       self.lights[ y * self.width + x ] = max(self.lights[ y * self.width + x ] - 1,0)

    def toggle(self, x, y):
       self.lights[ y * self.width + x ] += 2

def parse(string):
    for command in string.splitlines():
        match = re.match(r"(?P<command>turn\s+(?P<switch>on|off)|toggle)\s+(?P<start_x>[0-9]+),(?P<start_y>[0-9]+)\s+through\s+(?P<end_x>[0-9]+),(?P<end_y>[0-9]+)", command)
        if match:
           yield { "command": match.group("switch") or match.group("command"), "start": ( int(match.group("start_x")), int(match.group("start_y"))),  "end": ( int(match.group("end_x")), int(match.group("end_y"))) }

def iterate(instructions, grid):
    for instruction in instructions:
      command = getattr(grid, instruction["command"])
      for x in range(instruction["start"][0], instruction["end"][0]+1):
        for y in range(instruction["start"][1], instruction["end"][1]+1):
         command(x,y)

def solution(string, type_grid):
    grid = type_grid()

    iterate(parse(string), grid)

    return grid.brightness()

import functools

one = functools.partial(solution, type_grid=GridOne)
two = functools.partial(solution, type_grid=GridTwo)

