from dataclasses import dataclass


def get_input_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")


@dataclass(frozen=True)
class Point:
    x: int
    y: int