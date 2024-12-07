# test.txt
# its 143
from dataclasses import dataclass


def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

@dataclass
class PrintRule:
    first: int
    second: int

def get_rules(lines):
    rules = []
    in_rules = True
    for line in lines:
        if line == "":
            in_rules = False
            continue
        if not in_rules:
            continue
        first, second = line.split("|")
        rules.append(PrintRule(int(first), int(second)))
    return rules

rules = get_rules(get_input_lines("test.txt"))
assert len(rules) == 21

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 28

