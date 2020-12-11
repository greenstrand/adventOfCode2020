from .solvers import DefaultSolver
from .machine import Machine, InfiniteLoopError, CommandOutOfBoundsError


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return Machine.parse_instructions(lines)

    @staticmethod
    def part_1(data):
        m = Machine(data)
        try:
            m.execute()
            raise RuntimeError("Expected to fail.")
        except InfiniteLoopError:
            pass
        return m.accum

    @staticmethod
    def part_2(commands):
        for idx in range(len(commands)):
            orig = commands[idx]
            if orig.cmd not in ("nop", "jmp"):
                continue

            try:
                copy = list(commands)
                copy[idx] = orig._with(cmd=("nop" if orig.cmd == "jmp" else "jmp"))
                return Machine(copy).execute()
            except (InfiniteLoopError, CommandOutOfBoundsError):
                continue
        return None
