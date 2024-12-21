from typing import Tuple, List

from helpers.helpers import get_input_lines


def get_split_input_lines(filename: str) -> list[list[str]]:
    lines = get_input_lines(filename)
    split_lines = [line.split("   ") for line in lines]
    assert all(len(line) == 2 for line in split_lines)
    assert all(line[0].isdigit() and line[1].isdigit() for line in split_lines)
    return split_lines

def split_lines_to_two_lists(split_lines: list[list[str]]) -> tuple[list[str], list[str]]:
    list1 = []
    list2 = []
    for line in split_lines:
        list1.append(line[0])
        list2.append(line[1])
    return list1, list2

def calculate_difference(sorted_pairs: List[Tuple[str, str]]) -> int:
    return sum(abs(int(pair[0]) - abs(int(pair[1]))) for pair in sorted_pairs)

real_split_lines = get_split_input_lines("input.txt")
real_list1, real_list2 = split_lines_to_two_lists(real_split_lines)

real_sorted_pairs = list(zip(sorted(real_list1), sorted(real_list2)))

print()
print("About to calc")
difference = calculate_difference(real_sorted_pairs)
assert difference == 1660292
print (f"DIFFERENCE={difference}")




