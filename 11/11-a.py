def get_input_line(filename):
    with open(filename, "r") as file:
        return file.read()

test_line = get_input_line("test.txt")
assert len(test_line) == 6

def get_stones_from_line(line: str) -> list[int]:
    return [int(x) for x in line.split(" ")]

test_stones = get_stones_from_line(test_line)
assert test_stones == [125, 17]

def get_next_stones(stone: int) -> list[int]:
    str_stone = str(stone)
    len_str_stone = len(str_stone)
    if stone == 0:
        return [1]
    elif len_str_stone % 2 == 0:
        return [int(str_stone[: len_str_stone//2]), int(str_stone[len_str_stone//2: ])]
    else:
        return [stone * 2024]

assert get_next_stones(0) == [1]
assert get_next_stones(12) == [1, 2]
assert get_next_stones(123) == [123 * 2024]
assert get_next_stones(1000) == [10, 0]
assert get_next_stones(1234) == [12, 34]
assert get_next_stones(12345) == [12345 * 2024]
assert get_next_stones(123456) == [123, 456]