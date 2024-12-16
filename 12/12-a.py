from collections import defaultdict
import numpy as np
from typing import List, Dict, Tuple, Set

def get_input_lines(filename: str) -> List[str]:
    with open(filename, "r") as file:
        lines = file.read()
    assert "-" not in lines
    return lines.split("\n")

toy1_lines = get_input_lines('toy1.txt')
assert len(toy1_lines) == 4
test_lines = get_input_lines('test.txt')
assert len(test_lines) == 10

# TODO: continue from here

class Board:
    def __init__(self, lines: List[str]):
        self.lines = [list(l) for l in lines]
        assert all(len(row) == len(self.lines[0]) for row in self.lines)

    def get(self, x: int, y: int) -> str:
        if x not in self.get_x_range() or y not in self.get_y_range():
            return "-"
        else:
            return self.lines[y][x]

    def get_x_range(self) -> range:
        return range(len(self.lines[0]))

    def get_y_range(self) -> range:
        return range(len(self.lines))

test_board = Board(test_lines)

assert test_board.get(4, 4) == "0"
assert test_board.get(-1, 6) == "-"
assert test_board.get(6, 5) == "A"
assert test_board.get(4, -1) == "-"

def make_point_nparray(x: int, y: int) -> np.ndarray:
    return np.array([x, y])

def get_frequencies(board: Board) -> Dict[str, List[np.ndarray]]:
    frequencies = defaultdict(list)
    for y in board.get_y_range():
        for x in board.get_x_range():
            val = board.get(x, y)
            if val != ".":
                frequencies[val].append(np.array([x, y]))
    return frequencies

test_frequencies = get_frequencies(test_board)
assert len(test_frequencies) == 2
assert len(test_frequencies["0"]) == 4
assert len(test_frequencies["A"]) == 3
assert (test_frequencies["0"][0] == np.array((8, 1))).all()
assert (test_frequencies["0"][3] == np.array((4, 4))).all()

def get_pairs(board: Board, frequency: str) -> List[Tuple[np.ndarray, np.ndarray]]:
    pairs = []
    points = get_frequencies(board).get(frequency)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs.append((points[i], points[j]))
    return pairs

test_pairs1 = get_pairs(test_board, "0")
assert len(test_pairs1) == 6
assert (make_point_nparray(8, 1) == test_pairs1[2][0]).all()
assert (make_point_nparray(4, 4) == test_pairs1[2][1]).all()

def get_antinodes_for_pair(board: Board, pair: Tuple[np.ndarray, np.ndarray]) -> Set[Tuple[int, int]]:
    p1, p2 = pair
    antinodes = set()
    for start, delta in (p2, p2 - p1), (p1, p1 - p2):
        i = 0
        while True:
            candidate = start + i * delta
            if board.get(candidate[0], candidate[1]) == "-":
                break
            antinodes.add(tuple(candidate))
            i += 1
    return antinodes

test_antinodes1 = get_antinodes_for_pair(test_board, (make_point_nparray(8, 1), make_point_nparray(6, 2)))
assert len(test_antinodes1) == 6
assert (4, 3) in test_antinodes1
assert (10, 0) in test_antinodes1
assert (2, 4) in test_antinodes1
assert (0, 5) in test_antinodes1
assert (8, 1) in test_antinodes1
assert (6, 2) in test_antinodes1

def get_all_antinodes(board: Board, frequencies: Dict[str, List[np.ndarray]]) -> Set[Tuple[int, int]]:
    antinodes = set()
    for frequency in frequencies:
        for pair in get_pairs(board, frequency):
            antinodes |= get_antinodes_for_pair(board, pair)
    return antinodes

test_antinodes = get_all_antinodes(test_board, test_frequencies)
assert len(test_antinodes) == 34

real_lines = get_input_lines('input.txt')
real_board = Board(real_lines)
real_frequencies = get_frequencies(real_board)
real_antinodes = get_all_antinodes(real_board, real_frequencies)
assert len(real_antinodes) == 927
print(f"ANSWER: {len(real_antinodes)}")