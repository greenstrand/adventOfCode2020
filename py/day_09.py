from .solvers import DefaultSolver
import itertools

N = 25


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return list(map(int, lines))

    @staticmethod
    def part_1(data):
        return get_bad_num(data)

    @staticmethod
    def part_2(data):
        target = get_bad_num(data)

        result = get_summing_nums(data, target)
        if result:
            start, end = result
            nums = data[start:end]
            return min(nums) + max(nums)

        return None


def get_summing_nums(data, target):
    total = 0
    j = 0
    for i in range(len(data)):
        while total < target:
            j += 1
            total += data[j - 1]
        if total == target:
            return i, j
        total -= data[i]
    return None


def get_bad_num(data):
    for idx in range(N, len(data)):
        prev_set = set(data[idx - N : idx])
        if not get_matching_set(prev_set, 2, data[idx]):
            return data[idx]
    return None


def get_matching_set(number_set, count, _sum):
    for tpl in itertools.combinations(number_set, count):
        if sum(tpl) == _sum:
            return tpl
    return None
