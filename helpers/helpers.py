from dataclasses import dataclass

import numpy as np


def get_input_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.read()
    return lines.split("\n")


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def as_vector(self) -> np.ndarray:
        return np.array([self.x, self.y])

