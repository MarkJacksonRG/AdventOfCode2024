from dataclasses import dataclass
from datetime import datetime


def get_input_line(filename):
    with open(filename, "r") as file:
        return file.read()

test_line = get_input_line("test.txt")
assert len(test_line) == 6

@dataclass(frozen=True)
class Stone:
    value: int
    count: int = 1

def get_stones_from_line(line: str) -> list[Stone]:
    return [Stone(value=int(x)) for x in line.split(" ")]

test_stones = get_stones_from_line(test_line)
assert test_stones == [Stone(value=125), Stone(value=17)]

def get_next_stones(current: Stone) -> list[Stone]:
    str_stone = str(current.value)
    len_str_stone = len(str_stone)
    if current.value == 0:
        return [Stone(value=1, count=current.count)]
    elif len_str_stone % 2 == 0:
        return [
            Stone(value=int(str_stone[: len_str_stone//2]), count=current.count),
            Stone(value=int(str_stone[len_str_stone//2: ]), count=current.count)
        ]
    else:
        return [Stone(value= current.value * 2024, count=current.count)]

for count in range(1, 3):
    assert get_next_stones(Stone(value=0, count=count)) == [Stone(value=1, count=count)]
    assert get_next_stones(Stone(value=12, count=count)) == [Stone(value=1, count=count), Stone(value=2, count=count)]
    assert get_next_stones(Stone(value=123, count=count)) == [Stone(value=123 * 2024, count=count)]
    assert get_next_stones(Stone(value=1000, count=count)) == [Stone(value= 10, count=count), Stone(value= 0, count=count)]
    assert get_next_stones(Stone(value=1234, count=count)) == [Stone(value= 12, count=count), Stone(value= 34, count=count)]
    assert get_next_stones(Stone(value=12345, count=count)) == [Stone(value=12345 * 2024, count=count)]
    assert get_next_stones(Stone(value=123456, count=count)) == [Stone(value=123, count=count), Stone(value=456, count=count)]

def blink_stones(stones: list[Stone]) -> list[Stone]:
    new_stones = []
    for stone in stones:
        new_stones.extend(get_next_stones(stone))
    return new_stones

assert blink_stones([Stone(value=0), Stone(value=1), Stone(value=10), Stone(value=99), Stone(value=999)]) == [
    Stone(value=1), Stone(value=2024), Stone(value=1), Stone(value=0), Stone(value=9), Stone(value=9),
    Stone(value=2021976)]

def compress_stones(stones: list[Stone]) -> list[Stone]:
    compressed = {}
    for stone in stones:
        if stone.value in compressed:
            compressed[stone.value] += stone.count
        else:
            compressed[stone.value] = stone.count
    return [Stone(value=k, count=v) for k, v in compressed.items()]

assert compress_stones([Stone(value=1), Stone(value=1, count=2), Stone(value=2), Stone(value=3, count=3), Stone(value=2, count=4)]) == [
    Stone(value=1, count=3), Stone(value=2, count=5), Stone(value=3, count=3)]

def how_many_stones_after_blinks(stones: list[Stone], n: int) -> int:
    for i in range(n):
        print(f"{datetime.now()} - {i} - {len(stones)} - {len(set(stones))}")
        stones = compress_stones(blink_stones(stones))
    return sum(s.count for s in stones)

test_num_stones = how_many_stones_after_blinks(test_stones, 25)
assert test_num_stones == 55312

real_line = get_input_line("input.txt")
real_stones = get_stones_from_line(real_line)
real_num_stones = how_many_stones_after_blinks(real_stones, 25)
assert real_num_stones == 203953
print(f"ANSWER 11a = {real_num_stones}")

real_num_stones2 = how_many_stones_after_blinks(real_stones, 75)
print(f"ANSWER 11b = {real_num_stones2}")
