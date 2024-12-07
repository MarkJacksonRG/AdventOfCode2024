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
        if x not in self.get_x_range() or y not in self.get_y_range():
            return "."
        else:
            return self.dotted[y][x]

    def get_x_range(self):
        return range(len(self.dotted[0]))

    def get_y_range(self):
        return range(len(self.dotted))

    def get_trifecta(self, x, y, direction):
        as_list = [self.get(x + delta * direction[0], y + delta * direction[1]) for delta in (-1, 0, 1)]
        return ''.join(as_list)

test_board = Board(test_lines)

assert test_board.get(4, 1) == "X"
assert test_board.get(-1, -1) == "."
assert test_board.get_trifecta(1, 1, (1, 1)) == "MSX"
assert test_board.get_trifecta(1, 1, (-1, 1)) == "MSA"

def count_all_x_mas(board: Board):
    count = 0
    all_mas = ["MAS", "SAM"]
    for x in board.get_x_range():
        for y in board.get_y_range():
            t1 = board.get_trifecta(x, y, (1, 1))
            t2 = board.get_trifecta(x, y, (-1, 1))
            if t1 in all_mas and t2 in all_mas:
                count += 1
    return count

ret = count_all_x_mas(test_board)
assert ret == 9

real_lines = get_input_lines("input.txt")
real_board = Board(real_lines)
ret = count_all_x_mas(real_board)
print(f"XMAS COUNT={ret}")