from solvers import DefaultSolver, prod
from itertools import count


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return [[char == "#" for char in line] for line in lines]

    @staticmethod
    def part_1(grid):
        return count_trees(grid, 3, 1)

    @staticmethod
    def part_2(grid):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        num_trees = [count_trees(grid, dcol, drow) for dcol, drow in slopes]
        return prod(num_trees)


def count_trees(grid, dcol, drow):
    coords = zip(range(0, len(grid), drow), count(0, dcol))
    return sum(grid[row][col % len(grid[row])] for row, col in coords)
