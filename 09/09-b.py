import copy
from typing import List, Optional

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
assert toy_layout[1:3] == [-1] * 2
assert toy_layout[3:6] == [1] * 3
assert toy_layout[6:10] == [-1] * 4
assert toy_layout[10:15] == [2] * 5

def layout_from_string_of_blocks(string_of_blocks: str) -> List[int]:
    return [-1 if x == "." else int(x) for x in string_of_blocks]

test_layout = get_disk_layout(test_line)
expected_test_layout = layout_from_string_of_blocks("00...111...2...333.44.5555.6666.777.888899")
assert len(test_layout) == len(expected_test_layout)
assert test_layout == expected_test_layout

def attempt_move(compacted_layout: List[int], current_start: int, current_end: int, block_id: int) -> None:
    block_len = current_end - current_start + 1
    i = 0
    candidate_start: Optional[int] = None
    while i < current_start + 1:  # if there's free space immediately before the block, it can move
        if compacted_layout[i] == -1:
            if candidate_start is None:
                candidate_start = i
        else:
            if candidate_start is not None:
                if i - candidate_start >= block_len:
                    # We can move the block
                    for j in range(block_len):
                        compacted_layout[candidate_start + j] = block_id
                        compacted_layout[current_start + j] = -1
                    return
                candidate_start = None
        i += 1

def get_compact_layout(layout: List[int]) -> List[int]:
    compacted_layout = copy.deepcopy(layout)
    current_id = max(layout)
    while current_id >= 0:
        start = next((i for i, x in enumerate(compacted_layout) if x == current_id), None)
        assert start is not None
        end = start
        while end + 1 < len(compacted_layout) and compacted_layout[end + 1] == current_id:
            end += 1
        attempt_move(compacted_layout, start, end, current_id)
        current_id -= 1
        print("Current ID:", current_id)
    return compacted_layout

test_compact_layout = get_compact_layout(test_layout)
expected_test_compact_layout = layout_from_string_of_blocks("00992111777.44.333....5555.6666.....8888..")
assert len(test_compact_layout) == len(expected_test_compact_layout)
assert test_compact_layout == expected_test_compact_layout

def get_checksum(layout: List[int]) -> int:
    return sum(
        i * max(0, layout[i]) for i in range(len(layout))
    )

assert get_checksum(test_compact_layout) == 2858

real_layout = get_disk_layout(real_line)
real_compact_layout = get_compact_layout(real_layout)
real_checksum = get_checksum(real_compact_layout)
assert real_checksum == 6511178035564
print(f"ANSWER: {real_checksum}")