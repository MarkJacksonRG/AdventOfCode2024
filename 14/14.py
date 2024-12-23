from dataclasses import dataclass

import pytest

import numpy as np

from helpers.helpers import get_input_lines

@dataclass(frozen=True)
class Robot:
    p: np.array
    v: np.array

def to_2d_array(s: str) -> np.array:
    assert s[1] == "="
    return np.array([int(x) for x in s[2:].split(",")])

def get_robots_from_lines(lines: list[str]) -> list[Robot]:
    robots = []
    for line in lines:
        by_spaces = line.split(" ")
        pos = to_2d_array(by_spaces[0])
        direction = to_2d_array(by_spaces[1])
        robots.append(Robot(pos, direction))
    return robots

def get_p_after_t(r: Robot, t: int, space: np.array) -> np.array:
    return (r.p + r.v * t) % space

@pytest.fixture
def test_input():
    return get_input_lines("test.txt")

def test_get_input_lines(test_input):
    assert len(test_input) == 12

def test_get_robots_from_lines(test_input):
    robots = get_robots_from_lines(test_input)
    assert len(robots) == 12
    assert (robots[0].p == np.array([0, 4])).all()
    assert (robots[0].v == np.array([3, -3])).all()
    assert (robots[1].p == np.array([6, 3])).all()
    assert (robots[1].v == np.array([-1, -3])).all()

def test_get_p_after_t():
    space = np.array([11, 7])
    r = Robot(np.array([2, 4]), np.array([2, -3]))

    assert (get_p_after_t(r, 0, space) == np.array([2, 4])).all()
    assert (get_p_after_t(r, 1, space) == np.array([4, 1])).all()
    assert (get_p_after_t(r, 2, space) == np.array([6, 5])).all()
    assert (get_p_after_t(r, 3, space) == np.array([8, 2])).all()