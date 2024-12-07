# test.txt
# XMAS occurs 18 times

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()

    # split into separate lines
    return lines.split("\n")

test_lines = get_input_lines("03/04/test.txt")
assert len(test_lines) == 10

def xmas_or_dot(lines):
    to_return = []
    for l in lines:
        s = [c if c in "XMAS" else "." for c in l]
        to_return.append(s)
    return to_return

test_ret = xmas_or_dot(["ZXMASZ", "XMAS"])
print(test_ret)
assert test_ret[0] == list(".XMAS.")
assert test_ret[1] == list("XMAS")

# TODO refactor! here x means up/down and y means left/right!!
def get_directions(lines, x, y, c):
    to_return = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= len(lines):
                continue
            if new_y < 0 or new_y >= len(lines[new_x]):
                continue
            if (lines[new_x][new_y] == c):
                to_return.append((dx, dy))
    return to_return

test_dotted = xmas_or_dot(test_lines)

assert test_dotted[1][4] == "X"
ret = get_directions(test_dotted, 1, 4, "M")
assert ret == [(0, -1), (0, 1), (1, 1)]

def count_xmas(lines, x, y):
    count = 0
    for dx, dy in get_directions(lines, x, y, "M"):
        if (lines[x + 2*dx][y + 2*dy] == "A"):
            if (lines[x + 3*dx][y + 3*dy] == "S"):
                count += 1
    return count

ret = count_xmas(test_dotted, 1, 4)
assert ret == 1
