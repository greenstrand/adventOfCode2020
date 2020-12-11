from .solvers import DefaultSolver
from collections import Counter
from itertools import chain, product, count

import numpy as np


_neighbors = [(i, j) for (i, j) in product(range(-1, 2), range(-1, 2)) if i != 0 or j != 0]


LIVE = "#"
DEAD = "L"
EMPTY = "."


def count_neighbors(i, j, gg):
    count = 0
    for di, dj in _neighbors:
        count += gg[i + di, j + dj] == LIVE
    return count


def count_visible(i, j, gg):
    total = 0
    for di, dj in _neighbors:
        for x in count(1):
            res = gg[i + x * di, j + x * dj]
            if res == LIVE:
                total += 1
            if res != EMPTY:
                break
    return total


def show(grid):
    for line in grid:
        print("".join(line))


def counts(grid):
    return Counter(chain.from_iterable(grid))


def step_next(grid, count_fn, threshold, clone):
    for i, j in product(range(1, grid.shape[0] - 1), range(1, grid.shape[1] - 1)):
        if grid[i][j] == EMPTY:
            continue
        occupied = grid[i][j] == LIVE
        neighbors = count_fn(i, j, grid)

        if not occupied and not neighbors:
            clone[i][j] = LIVE
        elif occupied and neighbors >= threshold:
            clone[i][j] = DEAD
        else:
            clone[i][j] = grid[i][j]


def simulate(grid, count_fn, threshold):
    grid = np.pad(grid.copy(), pad_width=1, mode="constant", constant_values=None)
    clone = grid.copy()
    while True:
        step_next(grid, count_fn, threshold, clone)
        if np.array_equal(grid, clone):
            return clone
        grid, clone = clone, grid


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return np.array([list(l) for l in lines])

    @staticmethod
    def part_1(grid):
        grid = simulate(grid.copy(), count_neighbors, 4)
        return counts(grid)[LIVE]

    @staticmethod
    def part_2(grid):
        grid = simulate(grid.copy(), count_visible, 5)
        return counts(grid)[LIVE]
