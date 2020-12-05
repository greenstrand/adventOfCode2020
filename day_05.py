from solvers import DefaultSolver


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        output = []
        for line in lines:
            fb = line[:7]
            fb = [0 if x == "F" else 1 for x in fb]
            lr = line[7:]
            lr = [0 if x == "L" else 1 for x in lr]
            output.append((fb, lr))
        return output

    @staticmethod
    def part_1(data):
        output = []
        for fb, lr in data:
            # print(fb, lr)
            output.append((get_index(fb), get_index(lr)))

        ids = [row * 8 + col for row, col in output]
        print(ids)
        return max(ids)

    @staticmethod
    def part_2(data):
        output = []
        for fb, lr in data:
            # print(fb, lr)
            output.append((get_index(fb), get_index(lr)))

        ids = [row * 8 + col for row, col in output]
        max_id = 128 * 8
        missing = set(range(max_id)) - set(ids)
        return missing

def get_index(bits):
    output = 0
    for i, b in enumerate(reversed(bits)):
        output += b * (1 << i)
    return output
