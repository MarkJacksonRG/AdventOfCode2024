from collections import defaultdict, namedtuple
from dataclasses import dataclass
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

assert test_board.get(4, 1) == "I"
assert test_board.get(-1, 6) == "-"
assert test_board.get(4, -1) == "-"

# TODO: continue from here
@dataclass
class Point:
    x: int
    y: int

class Region:
    _points: Set[Point]

    def __init__(self, plant: str):
        self._points = set()
        self.plant = plant

    def add(self, point: Point):
        self._points.add(point)

    def contains(self, point: Point) -> bool:
        return point in self._points

    def area(self):
        return len(self._points)

def find_regions(board: Board) -> tuple[list[Region], dict[Point, Region]]:
    regions: List[Region] = []
    point_to_region: Dict[Point, Region] = {}

    for y in board.get_y_range():
        for x in board.get_x_range():
            point = Point(x, y)
            plant = board.get(x, y)
            region: Region | None = None
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if region is None and board.get(x + dx, y + dy) == plant:
                    if (neighbour := Point(x + dx, y + dy)) in point_to_region:
                        region = point_to_region[neighbour]
            if region is None:
                region = Region(plant)
                regions.append(region)
            region.add(point)
            point_to_region[point] = region
    return regions, point_to_region