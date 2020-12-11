from .solvers import DefaultSolver
from itertools import starmap


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return [bits_to_int([x in "BR" for x in line]) for line in lines]

    @staticmethod
    def part_1(ids):
        return max(ids)

    @staticmethod
    def part_2(ids):
        missing = set(range(min(ids), max(ids) + 1)) - set(ids)
        assert len(missing) == 1
        return missing.pop()


def bits_to_int(bits):
    return sum(int(b) * (1 << i) for i, b in enumerate(reversed(bits)))
