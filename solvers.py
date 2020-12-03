import abc
import functools
import operator


class BaseSolver(abc.ABC):
    @abc.abstractmethod
    def load_input(self, f):
        pass

    @abc.abstractmethod
    def part_1(self, data):
        pass

    @abc.abstractmethod
    def part_2(self, data):
        pass


def prod(nums):
    return functools.reduce(operator.mul, nums, 1)
