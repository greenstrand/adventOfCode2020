from solvers import DefaultSolver
from collections import Counter
from itertools import takewhile

from functools import lru_cache


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        data = sorted(map(int, lines))
        return [0] + data + [data[-1] + 3]

    @staticmethod
    def part_1(data):
        diffs = [data[i] - data[i - 1] for i in range(1, len(data))]
        counts = Counter(diffs)
        return counts[1] * counts[3]

    @staticmethod
    def part_2(data):
        counts = [1] * len(data)

        for i in range(1, len(data)):
            prev = takewhile(lambda j: data[j] + 3 >= data[i], range(i - 1, -1, -1))
            counts[i] = sum(counts[j] for j in prev)
        return counts[len(data) - 1]
