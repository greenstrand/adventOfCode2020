import re
from collections import namedtuple


pattern = r"^(?P<cmd>\w+) ?\+?(?P<num>[\-0-9.]+)"


class MachineError(Exception):
    pass


class CommandOutOfBoundsError(MachineError):
    pass


class InfiniteLoopError(MachineError):
    pass


class UnknownCommandError(MachineError):
    pass


class MachineInstruction(namedtuple("_MachineInstruction", ("cmd", "arg"))):
    def _with(self, **kwargs):
        d = self._asdict()
        d.update(**kwargs)
        return MachineInstruction(**d)


class Machine:
    INSTRUCTION_PATTERN = r"^(?P<cmd>\w+) ?(?P<arg>[+\-0-9.]+)"

    def __init__(self, codes):
        self.codes = codes
        self.curr = 0
        self.accum = 0
        self.step = 1

    def execute(self):
        visited = [False for x in self.codes]
        self.curr = 0
        self.accum = 0
        self.step = 0

        while True:
            if self.curr == len(self.codes):
                return self.accum
            if self.curr > len(self.codes):
                raise CommandOutOfBoundsError()
            if visited[self.curr]:
                raise InfiniteLoopError()
            visited[self.curr] = True

            self.step += 1
            cmd, arg = self.codes[self.curr]

            self._execute_command(cmd, arg)

    def _execute_command(self, cmd, arg):
        if cmd == "nop":
            self.curr += 1
        elif cmd == "acc":
            self.curr += 1
            self.accum += int(arg)
        elif cmd == "jmp":
            self.curr += int(arg)
        else:
            raise UnknownCommandError()

    @staticmethod
    def _parse_instruction(line, idx):
        try:
            return MachineInstruction(
                **re.match(Machine.INSTRUCTION_PATTERN, line).groupdict()
            )
        except Exception:
            print("Could not parse line {}: '{}'".format(idx, line))
            raise

    @staticmethod
    def parse_instructions(lines):
        return [Machine._parse_instruction(line, idx) for idx, line in enumerate(lines)]
