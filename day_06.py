from solvers import NestedGroupSolver, set_intersection, set_union


class Solver(NestedGroupSolver):
    @staticmethod
    def process_input(groups):
        return [[set(s) for s in group] for group in groups]

    @staticmethod
    def part_1(data):
        return sum(map(len, map(set_union, data)))

    @staticmethod
    def part_2(data):
        return sum(map(len, map(set_intersection, data)))
