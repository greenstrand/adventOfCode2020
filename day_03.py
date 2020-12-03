from solvers import BaseSolver, prod

class Solver(BaseSolver):
    @staticmethod
    def load_input(f):
        lines = list(f)
        return [[char == "#" for char in line.strip()] for line in lines if line.strip()]

    @staticmethod
    def part_1(grid):
        return count_trees(grid, 3, 1)

    @staticmethod
    def part_2(grid):
        slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        ]
        num_trees = [count_trees(grid, dcol, drow) for dcol, drow in slopes]
        return prod(num_trees)

def count_trees(grid, dcol, drow):
    col = 0
    count = 0
    for row in range(0, len(grid), drow):
        if grid[row][col % len(grid[0])]:
            count += 1
        col += dcol
    return count
