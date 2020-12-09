from solvers import DefaultSolver
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
        bad_num = get_bad_num(data)

        for i in range(len(data)):
            nums = get_summing_nums(i, data, bad_num)
            if nums:
                return min(nums) + max(nums)

        return None


def get_summing_nums(start, data, _sum):
    total = 0
    for i in range(start, len(data)):
        total += data[i]
        if total == _sum:
            return data[start : i + 1]
        elif total > _sum:
            return None
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
