import itertools
import functools
import operators

from solvers import BaseSolver

SUM = 2020


class Solver(BaseSolver):
    @staticmethod
    def load_input(f):
        return [int(s.strip()) for s in f if s.strip()]

    @staticmethod
    def part_1(number_set):
        result = get_matching_set(number_set, 2)
        print("Found:", *result)
        return prod(result)

    @staticmethod
    def part_2(number_set):
        result = get_matching_set(number_set, 3)
        print("Found:", *result)
        return prod(result)


def get_matching_set(number_set, count):
    for tpl in itertools.combinations(number_set, count):
        if sum(tpl) == SUM:
            return tpl
    return None


def prod(nums):
    return functools.reduce(operator.mul, nums, 1)
