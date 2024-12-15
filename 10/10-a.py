from typing import List

import numpy as np
import numpy.typing as npt


def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 8

class IntBoard:
    def __init__(self, lines):
        self.lines: List[List[str]] = [list(l) for l in lines]
        assert all(len(row) == len(self.lines[0]) for row in self.lines)

    def get(self, x: int, y: int) -> int:
        # x means left/right (positive is right) and y means up/down (positive is down)
        if x not in self.get_x_range() or y not in self.get_y_range():
            return -1
        else:
            return int(self.lines[y][x])

    def get_x_range(self):
        return range(len(self.lines[0]))

    def get_y_range(self):
        return range(len(self.lines))

test_board = IntBoard(test_lines)

assert test_board.get(4, 2) == 0
assert test_board.get(-1, 0) == -1
assert test_board.get(0, -1) == -1
assert test_board.get(8, 0) == -1
assert test_board.get(0, 8) == -1

class Scores:
    def __init__(self, board: IntBoard):
        self._x_range = board.get_x_range()
        self._y_range = board.get_y_range()
        self.scores: npt.NDArray[np.int_] = np.array([[-1 for _ in board.get_x_range()] for _ in board.get_y_range()])
        assert self.get(0,0) == -1
        assert self.get(board.get_x_range().stop-1, board.get_y_range().stop-1) == -1

    def get(self, x: int, y: int) -> int:
        if 0 <= x < self.scores.shape[1] and 0 <= y < self.scores.shape[0]:
            return int(self.scores[y][x])
        else:
            return -1

    def set(self, x: int, y: int, value: int):
        self.scores[y][x] = value

    def get_x_range(self):
        return self._x_range

    def get_y_range(self):
        return self._y_range


test_scores = Scores(test_board)
assert test_scores.get(0,0) == -1
test_scores.set(0,0,0)
assert test_scores.get(0,0) == 0
assert test_scores.get(-1,0) == -1
assert test_scores.get(0,-1) == -1
assert test_scores.get(8,0) == -1
assert test_scores.get(0,8) == -1

def get_scores(board: IntBoard):
    # Create numpy array of integers with the same dimensions as the board
    # and initialize it with -1
    scores = Scores(board)

    # Set all the trail ends to score 9
    for x in board.get_x_range():
        for y in board.get_y_range():
            if board.get(x, y) == 9:
                scores.set(x, y, 9)

    # Work backwards from trail end-1 to trail head
    # and set the score to the maximum of the scores of the adjacent cells
    for step_start in range(9-1, -1, -1):
        step_end = step_start + 1
        for x in board.get_x_range():
            for y in board.get_y_range():
                if board.get(x, y) == step_start:
                    step_score = max(
                        int(board.get(x + 1, y) == step_end) * scores.get(x + 1, y),
                        int(board.get(x - 1, y) == step_end) * scores.get(x - 1, y),
                        int(board.get(x, y + 1) == step_end) * scores.get(x, y + 1),
                        int(board.get(x, y + 1) == step_end) * scores.get(x, y - 1)
                    )
                    assert step_score in (0, 9), f"Invalid {step_score=}"
                    scores.set(x, y, step_score)
    return scores

def get_sum_trailhead_scores(board: IntBoard):
    scores = get_scores(board)
    return sum(scores.get(x, y) for x in scores.get_x_range() for y in scores.get_y_range() if board.get(x, y) == 0)

test_scores = get_scores(test_board)
test_sum_trailhead_scores = get_sum_trailhead_scores(test_board)
assert test_sum_trailhead_scores == 36