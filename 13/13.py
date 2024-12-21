from dataclasses import dataclass

from helpers.helpers import get_input_lines, Point

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 15

@dataclass(frozen=True)
class Machine:
    a: Point
    b: Point
    prize: Point

    def get_position(self, n_a: int, n_b: int) -> Point:
        return Point(
            n_a * self.a.x + n_b * self.b.x,
            n_a * self.a.y + n_b * self.b.y
        )

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
assert test_machines[0].get_position(1, 1) == Point(x=94+22, y=34+67)
assert test_machines[0].get_position(80, 40) == test_machines[0].prize
