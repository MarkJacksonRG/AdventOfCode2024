from dataclasses import dataclass


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
        self.lines = [list(l) for l in lines]
        assert all(len(row) == len(self.lines[0]) for row in self.lines)

    def get(self, x, y):
        # x means left/right (positive is right) and y means up/down (positive is down)
        if x not in self.get_x_range() or y not in self.get_y_range():
            return "-"
        else:
            return self.lines[y][x]

    def set(self, x, y, value):
        self.lines[y][x] = value

    def get_x_range(self):
        return range(len(self.lines[0]))

    def get_y_range(self):
        return range(len(self.lines))

# test set (and destroy the test board too!)
test_board = Board(test_lines)
assert test_board.get(4, 6) == "^"
test_board.set(4, 6, "!")
assert test_board.get(4, 6) == "!"

test_board = Board(test_lines)

assert test_board.get(4, 6) == "^"
assert test_board.get(-1, 6) == "-"
assert test_board.get(10, 6) == "-"
assert test_board.get(4, -1) == "-"
assert test_board.get(10, 10) == "-"

@dataclass
class Guard:
    x: int
    y: int
    direction: tuple[int, int]

    def move(self, board):
        if board.get(self.x + self.direction[0], self.y + self.direction[1]) == "#":
            self.direction = (-self.direction[1], self.direction[0])

        self.x += self.direction[0]
        self.y += self.direction[1]

        return self

test_guard = Guard(4, 6, (0, -1))
assert test_guard.move(test_board) == Guard(4, 5, (0, -1))
test_guard = Guard(4, 1, (0, -1))
assert test_guard.move(test_board) == Guard(5, 1, (1, 0))
test_guard = Guard(3, 0, (1, 0))
assert test_guard.move(test_board) == Guard(3, 1, (0, 1))

def count_positions_visited(board):
    # Find initial guard location: it's the first "^" anywhere in the board
    guard = None
    for y in board.get_y_range():
        for x in board.get_x_range():
            if board.get(x, y) == "^":
                guard = Guard(x, y, (0, -1))
                break
    assert guard is not None

    count = 0
    while board.get(guard.x, guard.y) != "-":
        if board.get(guard.x, guard.y) != "X":
            count += 1
        board.set(guard.x, guard.y, "X")
        guard.move(board)
    return count

assert count_positions_visited(test_board) == 41