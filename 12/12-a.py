from dataclasses import dataclass
from typing import List, Dict, Set


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

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class Region:
    points: Set[Point]

    def __init__(self, plant: str):
        self.points = set()
        self.plant = plant

    def add(self, point: Point):
        self.points.add(point)

    def add_points(self, points: Set[Point]):
        self.points |= points

    def contains(self, point: Point) -> bool:
        return point in self.points

    def area(self):
        return len(self.points)

    def perimeter(self):
        perimeter = 0
        for point in self.points:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbour = Point(point.x + dx, point.y + dy)
                if not self.contains(neighbour):
                    perimeter += 1
        return perimeter

def find_regions(board: Board) -> tuple[set[Region], dict[Point, Region]]:
    print("FIND REGIONS")
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
            region.add(point)
            point_to_region[point] = region

    # coalesce regions that are connected
    coalesced = True
    while coalesced:
        coalesced = False
        regions = set(point_to_region.values())
        print(f"  Coalescing: {len(regions)=}")
        for region in regions:
            connected_regions: Set[Region] = set()
            for point in region.points:
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbour = Point(point.x + dx, point.y + dy)
                    if board.get(neighbour.x, neighbour.y) == region.plant:
                        if neighbour not in region.points:
                            coalesced = True
                            print(f"    Coalescing {region.plant} at {point} with {neighbour}")
                            connected_regions.add(point_to_region[neighbour])
            if connected_regions:
                for connected_region in connected_regions:
                    for point in connected_region.points:
                        point_to_region[point] = region
                        region.add(point)
                    connected_region.points.clear()

    # remove empty regions
    regions = set(point_to_region.values())
    return regions, point_to_region

def get_price(regions: set[Region]) -> int:
    return sum(region.area() * region.perimeter() for region in regions)


def test_toy1():
    toy1_board = Board(toy1_lines)
    toy1_regions, toy1_point_to_region = find_regions(toy1_board)
    assert len(toy1_regions) == 5
    assert sum(region.area() for region in toy1_regions) == 16
    assert all(toy1_point_to_region[Point(x, y)].plant == plant for y, row in enumerate(toy1_lines) for x, plant in
               enumerate(row))
    toy1_region_A = toy1_point_to_region[Point(0, 0)]
    assert toy1_region_A.area() == 4
    assert toy1_region_A.perimeter() == 10
    assert toy1_region_A == toy1_point_to_region[Point(1, 0)]

    # toy1_region_A.add(Point(999, 999)) # TODO delete this
    # assert Point(999, 999) in toy1_point_to_region[Point(1, 0)].points # TODO delete this

    toy_region_B = toy1_point_to_region[Point(0, 1)]
    assert toy_region_B.plant == "B"
    assert toy_region_B.perimeter() == 8
    toy1_region_C = toy1_point_to_region[Point(2, 1)]
    assert toy1_region_C.plant == "C"
    assert toy1_region_C.area() == 4
    assert toy1_region_C.perimeter() == 10
    toy1_region_D = toy1_point_to_region[Point(3, 1)]
    assert toy1_region_D.plant == "D"
    assert toy1_region_D.area() == 1
    assert toy1_region_D.perimeter() == 4

    assert get_price(toy1_regions) == 140

test_toy1()



# TODO fix this
test_regions, test_point_to_region = find_regions(test_board)
assert len(test_regions) == 11
assert get_price(test_regions) == 1930