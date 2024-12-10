import copy
from dataclasses import dataclass


def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 10

class Board:
    def __init__(self, lines):
        self.lines = [list(l) for l in lines]
        self.visited: list[list[tuple[int, int]]] = []
        for l in lines:
            next_list: list[tuple[int, int]] = []
            self.visited.append(next_list)
            for c in l:
                next_list.append(list())
        assert all(len(row) == len(self.lines[0]) for row in self.lines)

    def get(self, x, y):
        # x means left/right (positive is right) and y means up/down (positive is down)
        if x not in self.get_x_range() or y not in self.get_y_range():
            return "-"
        else:
            return self.lines[y][x]

    def set(self, x, y, value):
        self.lines[y][x] = value

    def mark_visited(self, x, y, direction: tuple[int, int]):
        self.visited[y][x].append(direction)

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

def is_board_cycle(board: Board):
    # Find initial guard location: it's the first "^" anywhere in the board
    guard: Guard | None = None
    for y in board.get_y_range():
        for x in board.get_x_range():
            if board.get(x, y) == "^":
                guard = Guard(x, y, (0, -1))
                break
    assert guard is not None

    cycle = False
    while board.get(guard.x, guard.y) != "-":
        if guard.direction in board.visited[guard.y][guard.x]:
            cycle = True
            break
        board.mark_visited(guard.x, guard.y, guard.direction)
        guard.move(board)
    return cycle


test_cycle = is_board_cycle(test_board)
assert test_cycle == False

# Test the cycle detection mechanism by adding a cycle
cycle_board = Board(get_input_lines("test.txt"))
cycle_board.set(3, 6, "#")
cycle_cycle = is_board_cycle(cycle_board)
assert cycle_cycle == True

def count_obstacle_positions_that_cause_cycle(board: Board):
    reference_board = copy.deepcopy(board)
    initial_cycle = is_board_cycle(reference_board)
    assert initial_cycle == False

    count = 0
    for ox in reference_board.get_x_range():
        for oy in reference_board.get_y_range():
            print(f"{ox=}, {oy=}, {count=}")
            if not reference_board.visited[oy][ox]:
                continue
            if reference_board.get(ox, oy) == "^":
                continue
            candidate_board = copy.deepcopy(board)
            candidate_board.set(ox, oy, "#")
            if is_board_cycle(candidate_board):
                count += 1

    return count

# Get an unpolluted copy of test board
test_board = Board(test_lines)
test_count = count_obstacle_positions_that_cause_cycle(test_board)
assert test_count == 6

real_lines = get_input_lines("input.txt")
real_board = Board(real_lines)
real_cycle = is_board_cycle(real_board)
assert real_cycle == False

# Get an unpolluted copy of real board
real_board = Board(get_input_lines("input.txt"))
real_answer = count_obstacle_positions_that_cause_cycle(real_board)
print(f"ANSWER = {real_answer}")

# Apparently 1471 is too low