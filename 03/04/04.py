# test.txt
# XMAS occurs 18 times

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 10

def xmas_or_dot(lines):
    return [ [c if c in "XMAS" else "." for c in l] for l in lines ]

test_ret = xmas_or_dot(["ZXMASZ", "XMAS"])
print(test_ret)
assert test_ret[0] == list(".XMAS.")
assert test_ret[1] == list("XMAS")

class Board:
    def __init__(self, lines):
        self.dotted = xmas_or_dot(lines)
        assert all(len(row) == len(self.dotted[0]) for row in self.dotted)

    def get(self, x, y):
        # x means left/right and y means up/down
        try:
            return self.dotted[y][x]
        except IndexError:
            return '.'

    def get_x_range(self):
        return range(len(self.dotted[0]))

    def get_y_range(self):
        return range(len(self.dotted))

def get_directions(board: Board, x, y, c):
    to_return = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            if board.get(x + dx, y + dy) == c:
                to_return.append((dx, dy))
    return to_return

test_board = Board(test_lines)

assert test_board.get(4, 1) == "X"
ret = get_directions(test_board, 4, 1, "M")
assert ret == [(-1, 0), (1, 0), (1, 1)]

def count_xmas(board: Board, x, y):
    assert board.get(x, y) == "X", f"Expected X not {test_board.get(x, y)}"
    count = 0
    for dx, dy in get_directions(board, x, y, "M"):
        if board.get(x + 2 * dx, y + 2 * dy) == "A":
            if board.get(x + 3 * dx, y + 3 * dy) == "S":
                count += 1
    return count

#   0123456789
# 0 ....XXMAS. 0
# 1 .SAMXMS... 1
# 2 ...S..A... 2
# 3 ..A.A.MS.X 3
# 4 XMASAMX.MM 4
# 5 X.....XA.A 5
# 6 S.S.S.S.SS 6
# 7 .A.A.A.A.A 7
# 8 ..M.M.M.MM 8
# 9 .X.X.XMASX 9
#   0123456789
assert count_xmas(test_board, 4, 1) == 1
assert count_xmas(test_board, 4, 0) == 1
assert count_xmas(test_board, 4, 1) == 1
assert count_xmas(test_board, 3, 9) == 2
assert count_xmas(test_board, 4, 0) == 1
assert count_xmas(test_board, 6, 4) == 2

def count_all_xmas(board: Board):
    count = 0
    for x in board.get_x_range():
        for y in board.get_y_range():
            if board.get(x, y) == "X":
                count += count_xmas(board, x, y)
    return count

ret = count_all_xmas(test_board)
# assert ret == 18