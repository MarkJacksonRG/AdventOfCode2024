from dataclasses import dataclass

from helpers.helpers import get_input_lines, Point

test_lines = get_input_lines("test.txt")
assert len(test_lines) == 15

@dataclass(frozen=True)
class ButtonPresses:
    a: int
    b: int

    def __repr__(self):
        return f"ButtonPresses(a={self.a}, b={self.b})"

@dataclass(frozen=True)
class Machine:
    a: Point
    b: Point
    prize: Point

    def get_position(self, presses: ButtonPresses) -> Point:
        return Point(
            presses.a * self.a.x + presses.b * self.b.x,
            presses.a * self.a.y + presses.b * self.b.y
        )

    # def get_cheapest_prize(self) -> Point | None:


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
assert test_machines[0].get_position( ButtonPresses(1, 1)) == Point(x=94+22, y=34+67)
assert test_machines[0].get_position(ButtonPresses(80, 40)) == test_machines[0].prize
