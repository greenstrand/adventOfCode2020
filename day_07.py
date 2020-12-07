from solvers import DefaultSolver
import re

container_pattern = r"(.*) bags?"
pattern = r"(\d+) (.*) bags?.?"

COLOR = "shiny gold"


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        result = {}
        for line in lines:
            left, right = line.split("contain")

            container = re.match(container_pattern, left.strip()).group(1)
            contents = list(map(str.strip, right.split(",")))
            contents = (
                [re.match(pattern, s).groups() for s in contents]
                if contents != ["no other bags."]
                else []
            )
            contents = {bag: int(count) for count, bag in contents}
            result[container] = contents

        return result

    @staticmethod
    def part_1(data):
        def contains_color(node, color):
            children = data[node]
            if color in children:
                return True
            return any(contains_color(child, color) for child in children)

        return sum(contains_color(bag, COLOR) for bag in data)

    @staticmethod
    def part_2(data):
        def count_contents(node):
            total = 1
            for child in data[node]:
                total += count_contents(child) * data[node][child]
            return total

        total = count_contents(COLOR)
        # Subtract one for the root
        return total - 1
