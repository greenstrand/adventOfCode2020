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


def prod(nums):
    return functools.reduce(operator.mul, nums, 1)
