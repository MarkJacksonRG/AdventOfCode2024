import copy
from dataclasses import dataclass


def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 9

@dataclass
class Equation:
    result: int
    values: list[int]

def parse_line(line: str) -> Equation:
    parts = line.split(":")
    result = int(parts[0])
    values = [int(x) for x in parts[1].split(" ") if x.isdigit()]
    return Equation(result, values)

def parse_lines(lines: list[str]) -> list[Equation]:
    return [parse_line(line) for line in lines]

test_equations = parse_lines(test_lines)
assert len(test_equations) == 9
assert test_equations[0] == Equation(190, [10, 19])
assert test_equations[8] == Equation(292, [11, 6, 16, 20])

def get_candidates(equation: Equation) -> list[list[int | str]]:
    candidates = []

    def _get_stubs(candidate_stub: list[int | str], operator: str, i: int):
        candidate_stub.append(operator)
        candidate_stub.append(equation.values[i])
        if i == len(equation.values) - 1:
            candidates.append(candidate_stub)
            return
        _get_stubs(copy.deepcopy(candidate_stub), "+", i + 1)
        _get_stubs(copy.deepcopy(candidate_stub), "*", i + 1)


    def build_candidates():
        _get_stubs([equation.values[0]], "+", 1)
        _get_stubs([equation.values[0]], "*", 1)

    build_candidates()
    return candidates

test_candidates = get_candidates(test_equations[0])
assert len(test_candidates) == 2
assert test_candidates[0] == [10, "+", 19]
assert test_candidates[1] == [10, "*", 19]