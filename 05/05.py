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
    updates = []
    in_rules = True
    for line in lines:
        if line == "":
            in_rules = False
            continue
        if not in_rules:
            next_update = line.split(",")
            updates.append([int(x) for x in next_update])
            continue
        else:
            first, second = line.split("|")
            rules.append(PrintRule(int(first), int(second)))
    return rules, updates

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 28

rules, updates = get_rules(test_lines)
assert len(rules) == 21
assert rules[0] == PrintRule(47, 53)
assert len(updates) == 6
assert updates[0] == [75,47,61,53,29]

def is_update_in_right_order(update, rules):
    for rule in rules:
        if rule.first in update and rule.second in update:
            first_index = update.index(rule.first)
            second_index = update.index(rule.second)
            if first_index > second_index:
                return False
    return True

assert is_update_in_right_order(updates[0], rules) == True
assert is_update_in_right_order(updates[1], rules) == True
assert is_update_in_right_order(updates[2], rules) == True
assert is_update_in_right_order(updates[3], rules) == False
assert is_update_in_right_order(updates[4], rules) == False
assert is_update_in_right_order(updates[5], rules) == False
