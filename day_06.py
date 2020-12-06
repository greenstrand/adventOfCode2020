from solvers import BaseSolver


class Solver(BaseSolver):
    @staticmethod
    def process_input(f):
        data = f.read()
        groups = data.split("\n\n")
        groups = [group.split("\n") for group in groups]
        return groups

    @staticmethod
    def part_1(data):
        counts = [len(set("".join(group))) for group in data]
        return sum(counts)

    @staticmethod
    def part_2(data):
        all_sets = [len(reduce_sets(group)) for group in data]
        return sum(all_sets)


def reduce_sets(sets):
    res = set(sets[0])
    for s in sets:
        res = res & set(s)
    return res
