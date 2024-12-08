from dataclasses import dataclass
from functools import cmp_to_key


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

def custom_comparator(a, b, rules):
    a_b_rule = next((x for x in rules if x.first == a and x.second == b), None)
    if a_b_rule:
        return -1
    b_a_rule = next((x for x in rules if x.first == b and x.second == a), None)
    if b_a_rule:
        return 1
    # TODO perhaps handle transitive rules!?
    return 0

assert custom_comparator(47, 53, test_rules) == -1
assert custom_comparator(53, 47, test_rules) == 1
assert custom_comparator(47, 47, test_rules) == 0
assert custom_comparator(-1, -2, test_rules) == 0
assert custom_comparator(53, 13, test_rules) == -1
assert custom_comparator(13, 53, test_rules) == 1


def get_sum_of_middle_pages_for_sorted_invalid_updates(rules, updates):
    total = 0
    for update in updates:
        if not is_update_in_right_order(update, rules):
            sorted_update = sort_update(update, rules)
            total += middle_page(sorted_update)
    return total


def sort_update(update, rules):
    def custom_comparator_for_sort(a, b):
        return custom_comparator(a, b, rules)

    return list(sorted(update, key=cmp_to_key(custom_comparator_for_sort)))

assert sort_update([75,97,47,61,53], test_rules) == [97,75,47,61,53]

test_3 = get_sum_of_middle_pages_for_sorted_invalid_updates(test_rules, [test_updates[3]])
assert test_3 == 47

assert get_sum_of_middle_pages_for_sorted_invalid_updates(test_rules, test_updates) == 123

real_lines = get_input_lines("input.txt")
real_rules, real_updates = get_rules(real_lines)
print(f"ANSWER={get_sum_of_middle_pages_for_sorted_invalid_updates(real_rules, real_updates)}")