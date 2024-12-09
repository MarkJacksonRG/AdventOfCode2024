
def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 10

def xmas_or_dot(lines):
    return [ [c if c in "XMAS" else "." for c in l] for l in lines ]

class Board:
    def __init__(self, lines):
        self.lines = lines
        assert all(len(row) == len(self.lines[0]) for row in self.lines)

    def get(self, x, y):
        # x means left/right and y means up/down
        if x not in self.get_x_range() or y not in self.get_y_range():
            return "-"
        else:
            return self.lines[y][x]

    def get_x_range(self):
        return range(len(self.lines[0]))

    def get_y_range(self):
        return range(len(self.lines))

test_board = Board(test_lines)

assert test_board.get(4, 6) == "^"
assert test_board.get(-1, 6) == "-"
assert test_board.get(10, 6) == "-"
assert test_board.get(4, -1) == "-"
assert test_board.get(10, 10) == "-"
