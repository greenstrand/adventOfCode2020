from solvers import DefaultSolver
from itertools import starmap


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        output = []
        for line in lines:
            fb = bits_to_int([x != "F" for x in line[:7]])
            lr = bits_to_int([x != "L" for x in line[7:]])
            output.append((fb, lr))
        return output

    @staticmethod
    def part_1(data):
        ids = list(starmap(get_id, data))
        return max(ids)

    @staticmethod
    def part_2(data):
        ids = list(starmap(get_id, data))
        missing = set(range(min(ids), max(ids) + 1)) - set(ids)
        assert len(missing) == 1
        return missing.pop()


def bits_to_int(bits):
    return sum(int(b) * (1 << i) for i, b in enumerate(reversed(bits)))


def get_id(row, col):
    return row * 8 + col
