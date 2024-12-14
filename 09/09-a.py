from typing import List


def get_input_as_single_line(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read()

test_line = get_input_as_single_line('test.txt')
assert len(test_line) == 19

real_line = get_input_as_single_line('input.txt')
assert len(real_line) == 19_999
