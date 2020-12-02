import abc


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
