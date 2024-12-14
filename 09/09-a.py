from typing import List


def get_input_as_single_line(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read()

test_line = get_input_as_single_line('test.txt')
assert len(test_line) == 19

real_line = get_input_as_single_line('input.txt')
assert len(real_line) == 19_999

def get_disk_layout(line: str) -> List[int]:
    layout = []
    next_id = 0
    for i in range(0, len(line), 2):
        file_len = int(line[i])
        try:
            free_len = int(line[i + 1])
        except IndexError:
            free_len = 0
        layout.extend([next_id] * file_len)
        layout.extend([-1] * free_len)
        next_id += 1
    return layout

toy_layout = get_disk_layout("12345")
assert len(toy_layout) == 1 + 2 + 3 + 4 + 5
assert toy_layout[0] == 0
assert toy_layout[1] == -1
assert toy_layout[2] == -1
assert toy_layout[3] == 1
assert toy_layout[4] == 1
assert toy_layout[5] == 1
assert toy_layout[6] == -1
assert toy_layout[7] == -1
assert toy_layout[8] == -1
assert toy_layout[9] == -1

test_layout = get_disk_layout(test_line)
expected_test_layout = [
    -1 if x=="." else int(x) for x in "00...111...2...333.44.5555.6666.777.888899"]
assert len(test_layout) == len(expected_test_layout)