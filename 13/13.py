from dataclasses import dataclass

import numpy as np

from helpers.helpers import get_input_lines, Point

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 15

@dataclass(frozen=True)
class ButtonPresses:
    a: int
    b: int

    def as_vector(self) -> np.ndarray:
        return np.array([self.a, self.b], dtype=np.float64)

    def __repr__(self):
        return f"ButtonPresses(a={self.a}, b={self.b})"

    def price(self) -> int:
        return self.a * 3 + self.b


@dataclass(frozen=True)
class Machine:
    a: Point
    b: Point
    prize: Point

    def get_position(self, presses: ButtonPresses) -> Point:
        m = self.as_matrix()
        b = presses.as_vector()
        return Point(*np.dot(m, b))

    def as_matrix(self) -> np.ndarray:
        return np.array([[self.a.x, self.b.x], [self.a.y, self.b.y]], dtype=np.float64)

    def get_cheapest_prize_presses(self) -> ButtonPresses | None:
        m = self.as_matrix()
        p = self.prize.as_vector(dtype=np.float64)
        b_v_float = np.linalg.solve(m, p)
        b_v = np.round(b_v_float).astype(int)
        if not np.all(np.absolute(b_v_float - b_v) < 0.01):
            return None
        return ButtonPresses(b_v[0], b_v[1])

    def get_price_of_cheapest_prize_presses(self) -> int:
        cheapest_prize_presses = self.get_cheapest_prize_presses()
        if cheapest_prize_presses is None:
            return 0
        return cheapest_prize_presses.price()

    def __repr__(self):
        return f"Machine(a={self.a}, b={self.b}, prize={self.prize})"


def get_machines_from_lines(lines: list[str]) -> list[Machine]:
    machines = []
    i = 0
    while i < len(lines):
        a = get_point_from_button_line("A", lines[i])
        b = get_point_from_button_line("B", lines[i+1])
        prize = get_point_from_prize_line(lines[i+2])
        machines.append(Machine(a, b, prize))
        i += 4
    return machines

def get_point_from_button_line(button_name: str, line: str) -> Point:
    assert line[:10] == f"Button {button_name}: "
    button_bits = line[10:].split(", ")
    assert len(button_bits) == 2
    x = int(button_bits[0][2:])
    y = int(button_bits[1][2:])
    assert x >= 0 and y >=0
    return Point(x, y)

def get_point_from_prize_line(line) -> Point:
    assert line[:7] == "Prize: "
    prize_bits = line[7:].split(", ")
    assert len(prize_bits) == 2
    x = int(prize_bits[0][2:])
    y = int(prize_bits[1][2:])
    return Point(x, y)

test_machines = get_machines_from_lines(test_lines)
for m in test_machines:
    print(m)

assert test_machines[0] == Machine(a=Point(x=94, y=34), b=Point(x=22, y=67), prize=Point(x=8400, y=5400))
assert test_machines[0].get_position(ButtonPresses(1, 1)) == Point(x=94+22, y=34+67)
assert test_machines[0].get_position(ButtonPresses(80, 40)) == test_machines[0].prize

assert test_machines[0].get_cheapest_prize_presses() == ButtonPresses(80, 40)
assert test_machines[1].get_cheapest_prize_presses() is None
assert test_machines[2].get_cheapest_prize_presses() == ButtonPresses(38, 86)
assert test_machines[3].get_cheapest_prize_presses() is None

def get_min_tokens_to_win_all_prizes(machines: list[Machine]) -> int:
    return sum(m.get_price_of_cheapest_prize_presses() for m in machines)

test_min_tokens = get_min_tokens_to_win_all_prizes(test_machines)
assert test_min_tokens == 480

real_lines = get_input_lines("input.txt")
real_machines = get_machines_from_lines(real_lines)
real_min_tokens = get_min_tokens_to_win_all_prizes(real_machines)
assert real_min_tokens == 31761
print(f"Real min tokens: {real_min_tokens}")


def get_part_2_machines(machines):
    return [
        Machine(m.a, m.b, Point(m.prize.x + 10000000000000, m.prize.y + 10000000000000)) for m in machines
    ]

test_machines_2 = get_part_2_machines(test_machines)
assert test_machines_2[0].a == test_machines[0].a
assert test_machines_2[0].b == test_machines[0].b
assert test_machines_2[0].prize == Point(10000000008400, 10000000005400)
assert test_machines_2[0].get_cheapest_prize_presses() is None
assert test_machines_2[1].get_cheapest_prize_presses() is not None

real_machines_2 = get_part_2_machines(real_machines)
real_min_tokens_2 = get_min_tokens_to_win_all_prizes(real_machines_2)
assert real_min_tokens_2 == 90798500745591
print(f"Real min tokens: {real_min_tokens_2}")
