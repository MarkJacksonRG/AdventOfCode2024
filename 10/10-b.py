from typing import List, Set, Tuple

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

class Trails:
    def __init__(self, board: IntBoard):
        self._x_range = board.get_x_range()
        self._y_range = board.get_y_range()
        self.trails: List[List[List]] = [[[] for _ in board.get_x_range()] for _ in board.get_y_range()]

    def get(self, x: int, y: int) -> List:
        if x in self.get_x_range() and y in self.get_y_range():
            return self.trails[y][x]
        else:
            return []

    # def prepend_point(self, x: int, y: int, point: Tuple) -> None:
    #     for trail in self.get(x, y):
    #         trail.insert(0, point)

    def get_x_range(self):
        return self._x_range

    def get_y_range(self):
        return self._y_range

    def set(self, x: int, y: int, trails: List[List[Tuple]]):
        self.trails[y][x] = trails


test_trails = Trails(test_board)
assert test_trails.get(0, 0) == []
assert test_trails.get(-1, 0) == []
assert test_trails.get(0, -1) == []
assert test_trails.get(8, 0) == []
assert test_trails.get(0, 8) == []

def get_trails(board: IntBoard) -> Trails:
    trails = Trails(board)

    # Set all the trail ends as able to reach themselves
    for x in board.get_x_range():
        for y in board.get_y_range():
            if board.get(x, y) == 9:
                trails.set(x, y, [[(x, y)]])

    # Work backwards from level trail end-1 to trail head
    for step_start in range(9-1, -1, -1):
        step_end = step_start + 1
        for x in board.get_x_range():
            for y in board.get_y_range():
                if board.get(x, y) == step_start:
                    trails_for_cell = []
                    if board.get(x + 1, y) == step_end:
                        trails_for_cell += trails.get(x + 1, y)
                    if board.get(x - 1, y) == step_end:
                        trails_for_cell += trails.get(x - 1, y)
                    if board.get(x, y - 1) == step_end:
                        trails_for_cell += trails.get(x, y - 1)
                    if board.get(x, y + 1) == step_end:
                        trails_for_cell += trails.get(x, y + 1)
                    for trail in trails_for_cell:
                        trail.insert(0, (x, y))
                    trails.set(x, y, trails_for_cell)
    return trails

def get_sum_trailhead_scores(board: IntBoard, trails: Trails) -> int:

    return sum(len(trails.get(x, y)) for x in board.get_x_range() for y in board.get_y_range() if board.get(x, y) == 0)

test_trails = get_trails(test_board)
test_sum_trailhead_scores = get_sum_trailhead_scores(test_board, test_trails)
assert test_sum_trailhead_scores == 81

real_board = IntBoard(get_input_lines("input.txt"))
real_reachable_trailends = get_trails(real_board)
real_sum_trailhead_scores = get_sum_trailhead_scores(real_board, real_reachable_trailends)
assert real_sum_trailhead_scores == 1289
print(f"ANSWER: {real_sum_trailhead_scores}")