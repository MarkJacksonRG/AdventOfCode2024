# test.txt
# its 143
from dataclasses import dataclass
from os.path import realpath
from pickletools import read_long1


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

test_rules, test_updates = get_rules(test_lines)
assert len(test_rules) == 21
assert test_rules[0] == PrintRule(47, 53)
assert len(test_updates) == 6
assert test_updates[0] == [75, 47, 61, 53, 29]

def is_update_in_right_order(update, rules):
    for rule in rules:
        if rule.first in update and rule.second in update:
            first_index = update.index(rule.first)
            second_index = update.index(rule.second)
            if first_index > second_index:
                return False
    return True

assert is_update_in_right_order(test_updates[0], test_rules) == True
assert is_update_in_right_order(test_updates[1], test_rules) == True
assert is_update_in_right_order(test_updates[2], test_rules) == True
assert is_update_in_right_order(test_updates[3], test_rules) == False
assert is_update_in_right_order(test_updates[4], test_rules) == False
assert is_update_in_right_order(test_updates[5], test_rules) == False

def middle_page(a_list):
    return a_list[int(len(a_list) / 2)]

assert middle_page([75,47,61,53,29]) == 61

def get_sum_of_middle_pages_for_valid_updates(rules, updates):
    return sum([middle_page(update) for update in updates if is_update_in_right_order(update, rules)])

assert get_sum_of_middle_pages_for_valid_updates(test_rules, test_updates) == 143

real_lines = get_input_lines("input.txt")
real_rules, real_updates = get_rules(real_lines)
print(f"ANSWER={get_sum_of_middle_pages_for_valid_updates(real_rules, real_updates)}")