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

def blink_stones(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        new_stones.extend(get_next_stones(stone))
    return new_stones

assert blink_stones([0, 1, 10, 99, 999]) == [1, 2024, 1, 0, 9, 9, 2021976]

# def how_many_stones_after_blinks(stones: list[int], n: int) -> int:
#     for _ in range(n):
#         stones = blink_stones(stones)
#     return len(stones)
#
# assert how_many_stones_after_blinks(test_stones, 25) == 55312