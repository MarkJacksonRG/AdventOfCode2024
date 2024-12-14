from dataclasses import dataclass

import numpy as np


def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 12

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

assert test_board.get(4, 4) == "0"
assert test_board.get(-1, 6) == "-"
assert test_board.get(6, 5) == "A"
assert test_board.get(4, -1) == "-"

@dataclass(frozen=True)
class Point:
    x: int
    y: int

def get_frequencies(board: Board):
    frequencies = {}
    for y in board.get_y_range():
        for x in board.get_x_range():
            val = board.get(x, y)
            if val != ".":
                # TODO use defaultdict or setdefault
                if val not in frequencies:
                    frequencies[val] = []
                points = frequencies.get(val)
                points.append(np.array([x, y]))
    return frequencies

test_frequencies = get_frequencies(test_board)
assert len(test_frequencies) == 2
assert len(test_frequencies["0"]) == 4
assert len(test_frequencies["A"]) == 3
assert (test_frequencies["0"][0] == np.array((8, 1))).all()
assert (test_frequencies["0"][3] == np.array((4, 4))).all()

def get_pairs(board: Board, frequency: str):
    pairs = []
    points = get_frequencies(board).get(frequency)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs.append((points[i], points[j]))
    return pairs
test_pairs1 = get_pairs(test_board, "0")
assert len(test_pairs1) == 6
assert (Point(8, 1), Point(4, 4)) in test_pairs1
assert (Point(8, 1), Point(5, 2)) in test_pairs1
assert (Point(5, 2), Point(4, 4)) in test_pairs1

def get_antinodes_for_pair(board: Board, pair: tuple[Point, Point]) -> set[Point]:
    p1, p2 = pair
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    antinodes = set()
    for candidate in (Point(p1.x - dx, p1.y - dy), Point(p2.x + dx, p2.y + dy)):
        if board.get(candidate.x, candidate.y) != "-":
            antinodes.add(candidate)
    return antinodes

test_antinodes1 = get_antinodes_for_pair(test_board, (Point(8, 1), Point(6, 2)))
assert len(test_antinodes1) == 2
assert Point(4, 3) in test_antinodes1
assert Point(10, 0) in test_antinodes1