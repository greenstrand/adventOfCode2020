from .solvers import DefaultSolver
from collections import Counter
from itertools import chain, product, count


def get(i, j, gg):
    if i < 0 or i >= len(gg):
        return None
    if j < 0 or j >= len(gg[0]):
        return None
    return gg[i][j]


def neighbors():
    for di, dj in product(range(-1, 2), range(-1, 2)):
        if di != 0 or dj != 0:
            yield di, dj


def count_neighbors(i, j, gg):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            count += get(i + di, j + dj, gg) == "#"
    return count


def count_visible(i, j, gg):
    total = 0
    for di, dj in neighbors():
        if di == 0 and dj == 0:
            continue
        for x in count(1):
            res = get(i + x * di, j + x * dj, gg)
            if res == "#":
                total += 1
            if res != ".":
                break
    return total


def deequals(g1, g2):
    return all(l1 == l2 for l1, l2 in zip(g1, g2))


def show(grid):
    for line in grid:
        print("".join(line))


def counts(grid):
    return Counter(chain.from_iterable(grid))


def step_next(grid, count_fn, threshold):
    clone = [list(l) for l in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                continue
            occupied = grid[i][j] == "#"
            neighbors = count_fn(i, j, grid)

            if not occupied and not neighbors:
                clone[i][j] = "#"
            if occupied and neighbors >= threshold:
                clone[i][j] = "L"
    return clone


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return [list(l) for l in lines]

    @staticmethod
    def part_1(data):
        prev = data
        while True:
            curr = step_next(prev, count_neighbors, 4)
            if deequals(prev, curr):
                break
            prev = curr
        return counts(curr)["#"]

    @staticmethod
    def part_2(data):
        prev = data
        while True:
            curr = step_next(prev, count_visible, 5)
            if deequals(prev, curr):
                break
            prev = curr
        return counts(curr)["#"]
