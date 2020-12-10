from solvers import DefaultSolver
from collections import Counter

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
        @lru_cache(maxsize=2 * len(data))
        def count_arrangements(idx):
            if idx == 0:
                return 1
            elif idx < 0:
                return 0

            total = 0
            for j in range(idx - 1, -1, -1):
                if data[j] + 3 < data[idx]:
                    break
                total += count_arrangements(j)
            return total

        return count_arrangements(len(data) - 1)
