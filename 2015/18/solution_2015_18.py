import functools


class Grid:
    def __init__(self, rows):
        self.grid = [bytearray(1 if bulb == "#" else 0 for bulb in row) for row in rows]

    def _get_lit_neighbors(self, row, col):
        neighbors = []
        for i in range(row - 1, row + 2):
            if -1 < i < len(self.grid):
                neighbors.extend(
                    (i, j)
                    for j in range(col - 1, col + 2)
                    if -1 < j < len(self.grid[i])
                )
        neighbors.remove((row, col))
        return sum(self.grid[i][j] for i, j in neighbors)

    def step(self):
        rows = len(self.grid)
        cols = len(self.grid[0])
        grid = [bytearray(cols) for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                neighbors = self._get_lit_neighbors(row, col)
                if self.grid[row][col]:
                    grid[row][col] = 1 if neighbors in (2, 3) else 0
                else:
                    grid[row][col] = 1 if neighbors == 3 else 0
        self.grid = grid

    def count_lights(self):
        return sum(sum(row) for row in self.grid)


class StuckGrid(Grid):
    def stuck(self):
        self.grid[0][0] = self.grid[0][-1] = self.grid[-1][0] = self.grid[-1][-1] = 1

    def __init__(self, rows):
        super().__init__(rows)
        self.stuck()

    def step(self):
        super().step()
        self.stuck()


def solution(string, grid, steps):
    _grid = grid(string.splitlines())
    for _ in range(steps):
        _grid.step()
    return _grid.count_lights()


one = functools.partial(solution, grid=Grid, steps=100)
two = functools.partial(solution, grid=StuckGrid, steps=100)
