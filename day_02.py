from collections import Counter, namedtuple
import re

from solvers import DefaultSolver

Password = namedtuple("Password", ("letter", "min", "max", "password"))
PATTERN = r"(?P<min>\d+)-(?P<max>\d+) +(?P<letter>\w): +(?P<password>.*)"


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return [Password(**re.match(PATTERN, line).groupdict()) for line in lines]

    @staticmethod
    def part_1(passwords):
        def is_valid(p):
            counts = Counter(p.password)
            found = counts[p.letter]
            return found >= int(p.min) and found <= int(p.max)

        return len(list(filter(is_valid, passwords)))

    @staticmethod
    def part_2(passwords):
        def is_valid(p):
            has_first = p.password[int(p.min) - 1] == p.letter
            has_last = p.password[int(p.max) - 1] == p.letter
            return has_first != has_last

        return len(list(filter(is_valid, passwords)))
