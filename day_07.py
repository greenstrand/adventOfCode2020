from solvers import DefaultSolver
import re

container_pattern = r"^(?P<color>[^,.]+) bags? contain"
count_pattern = r"(?P<count>\d+) (?P<color>[^,.]+) bags?"

COLOR = "shiny gold"


class Solver(DefaultSolver):
    @staticmethod
    def process_input(lines):
        return {
            re.match(container_pattern, line)["color"]: {
                match["color"]: int(match["count"]) for match in re.finditer(count_pattern, line)
            }
            for line in lines
        }

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
