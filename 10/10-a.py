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

class ReachableTrailends:
    def __init__(self, board: IntBoard):
        self._x_range = board.get_x_range()
        self._y_range = board.get_y_range()
        self.reachable_trailends: List[List[Set]] = [[set() for _ in board.get_x_range()] for _ in board.get_y_range()]
        assert self.get(0,0) == set()
        assert self.get(board.get_x_range().stop-1, board.get_y_range().stop-1) == set()

    def get(self, x: int, y: int) -> Set:
        if x in self.get_x_range() and y in self.get_y_range():
            return self.reachable_trailends[y][x]
        else:
            return set()

    def merge_trailends(self, x: int, y: int, trailends: Set) -> None:
        self.reachable_trailends[y][x] |= trailends

    def get_x_range(self):
        return self._x_range

    def get_y_range(self):
        return self._y_range


test_reachable_trailends = ReachableTrailends(test_board)
assert test_reachable_trailends.get(0, 0) == set()
test_reachable_trailends.merge_trailends(0, 0, {(10, 10)})
assert test_reachable_trailends.get(0, 0) == {(10, 10)}
test_reachable_trailends.merge_trailends(0, 0, {(20, 20)})
assert test_reachable_trailends.get(0, 0) == {(10, 10), (20, 20)}
assert test_reachable_trailends.get(-1, 0) == set()
assert test_reachable_trailends.get(0, -1) == set()
assert test_reachable_trailends.get(8, 0) == set()
assert test_reachable_trailends.get(0, 8) == set()

def get_reachable_trailends(board: IntBoard) -> ReachableTrailends:
    reachable_trailends = ReachableTrailends(board)

    # Set all the trail ends as able to reach themselves
    for x in board.get_x_range():
        for y in board.get_y_range():
            if board.get(x, y) == 9:
                reachable_trailends.merge_trailends(x, y, {(x, y)})

    # Work backwards from trail end-1 to trail head
    # and set the reachable trailends as all the reachable trailends of the adjacent cells
    for step_start in range(9-1, -1, -1):
        step_end = step_start + 1
        for x in board.get_x_range():
            for y in board.get_y_range():
                if board.get(x, y) == step_start:
                    reachable_from_here = (
                        reachable_trailends.get(x + 1, y) |
                        reachable_trailends.get(x - 1, y) |
                        reachable_trailends.get(x, y + 1) |
                        reachable_trailends.get(x, y + 1)
                    )
                    reachable_trailends.merge_trailends(x, y, reachable_from_here)
    return reachable_trailends

def get_sum_trailhead_scores(board: IntBoard, reachable_trailends: ReachableTrailends) -> int:

    return sum(len(reachable_trailends.get(x, y)) for x in board.get_x_range() for y in board.get_y_range() if board.get(x, y) == 0)

test_reachable_trailends = get_reachable_trailends(test_board)
test_sum_trailhead_scores = get_sum_trailhead_scores(test_board, test_reachable_trailends)
assert test_sum_trailhead_scores == 36

real_board = IntBoard(get_input_lines("input.txt"))
real_reachable_trailends = get_reachable_trailends(real_board)
real_sum_trailhead_scores = get_sum_trailhead_scores(real_board, real_reachable_trailends)
print(f"ANSWER: {real_sum_trailhead_scores}")