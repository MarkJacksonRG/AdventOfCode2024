def get_input_line(filename):
    with open(filename, "r") as file:
        return file.read()

test_line = get_input_line("test.txt")
assert len(test_line) == 6

def get_stones_from_line(line: str) -> list[int]:
    return [int(x) for x in line.split(" ")]

test_stones = get_stones_from_line(test_line)
assert test_stones == [125, 17]