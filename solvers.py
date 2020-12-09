import abc
import functools
import operator


class BaseSolver(abc.ABC):
    def load_input(self, path):
        with open(path) as f:
            return self.process_input(f)

    @abc.abstractmethod
    def process_input(self, lines):
        pass

    @abc.abstractmethod
    def part_1(self, data):
        pass

    @abc.abstractmethod
    def part_2(self, data):
        pass


class DefaultSolver(BaseSolver):
    def load_input(self, path):
        with open(path) as f:
            return self.process_input(line.strip() for line in f if line.strip())


class NestedGroupSolver(BaseSolver):
    def load_input(self, path):
        with open(path) as f:
            groups = [[s.strip() for s in group.split("\n")] for group in f.read().split("\n\n")]
            return self.process_input(groups)


def prod(nums):
    return functools.reduce(operator.mul, nums, 1)


def set_union(sets):
    return functools.reduce(set.union, sets) if sets else set()


def set_intersection(sets):
    return functools.reduce(set.intersection, sets) if sets else set()
