import itertools

from .solvers import DefaultSolver, prod

SUM = 2020


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return [int(line) for line in lines]

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
