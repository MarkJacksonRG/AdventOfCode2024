import numpy as np


def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 8

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

    def get_x_range(self):
        return range(len(self.lines[0]))

    def get_y_range(self):
        return range(len(self.lines))

test_board = Board(test_lines)

assert test_board.get(4, 2) == "0"

def get_scores(board: Board):
    # Create numpy array of integers with the same dimensions as the board
    # and initialize it with -1
    scores = np.array([[-1 for _ in board.get_x_range()] for _ in board.get_y_range()])
    assert scores[0][0] == -1
    assert scores[board.get_x_range().stop-1][board.get_y_range().stop-1] == -1
    return scores

get_scores(test_board)