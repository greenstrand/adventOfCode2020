from solvers import DefaultSolver
import re


pattern = r"^(?P<cmd>\w+) ?\+?(?P<num>[\-0-9.]+)"


class CustomError(Exception):
    pass


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        matches = [re.match(pattern, line) for line in lines]
        return [(m["cmd"], int(m["num"])) for m in matches]

    @staticmethod
    def part_1(data):
        visited = set()

        curr_idx = 0
        accum = 0

        class Machine:
            def __init__(self):
                self.curr = 0
                self.accum = 0
                self.step = 1

            def execute_next(self):
                if self.curr >= len(data):
                    return False

                cmd, count = data[self.curr]
                if self.curr in visited:
                    return False

                visited.add(self.curr)
                self.step += 1

                if cmd == "nop":
                    self.curr += 1
                elif cmd == "acc":
                    self.curr += 1
                    self.accum += count
                elif cmd == "jmp":
                    self.curr += count
                else:
                    raise RuntimeError("Oh no!")

                return True

        m = Machine()

        while m.execute_next():
            pass
        return m.accum

        # return data

    @staticmethod
    def part_2(commands):
        class Machine:
            def __init__(self, data):
                self.data = data
                self.visited = set()
                self.curr = 0
                self.accum = 0
                self.step = 1

            def execute_next(self):
                if self.curr >= len(self.data):
                    return False

                cmd, count = self.data[self.curr]
                if self.curr in self.visited:
                    raise CustomError()

                self.visited.add(self.curr)
                self.step += 1

                if cmd == "nop":
                    self.curr += 1
                elif cmd == "acc":
                    self.curr += 1
                    self.accum += count
                elif cmd == "jmp":
                    self.curr += count
                else:
                    raise RuntimeError("Oh no!")

                return True

        for idx in range(len(commands)):
            if commands[idx][0] not in ("nop", "jmp"):
                continue

            try:
                changed = list(commands)
                cmd, count = changed[idx]
                changed[idx] = ("nop" if cmd == "jmp" else "jmp", count)
                m = Machine(changed)
                while m.execute_next():
                    pass
                return m.accum
            except CustomError:
                continue
        return None
