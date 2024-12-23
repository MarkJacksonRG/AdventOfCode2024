from dataclasses import dataclass

import pytest

import numpy as np

from helpers.helpers import get_input_lines

@dataclass(frozen=True)
class Robot:
    p: np.ndarray
    v: np.ndarray

def to_2d_array(s: str) -> np.ndarray:
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

def count_robots_on_position(positions: list[np.ndarray], p: np.ndarray) -> int:
    return sum([1 for next_p in positions if (next_p == p).all()])

def get_p_after_t(r: Robot, t: int, space: np.ndarray) -> np.ndarray:
    return (r.p + r.v * t) % space

def get_safety_factor(positions: list[np.ndarray], space: np.ndarray) -> int:
    tl, tr, bl, br = 0, 0, 0, 0
    mid_x, mid_y = int(space[0] / 2), int(space[1] / 2)
    for p in positions:
        if p[0] < mid_x and p[1] < mid_y:
            tl += 1
        elif p[0] > mid_x and p[1] < mid_y:
            tr += 1
        elif p[0] < mid_x and p[1] > mid_y:
            bl += 1
        elif p[0] > mid_x and p[1] > mid_y:
            br += 1
    return tl * tr * bl * br


real_input = get_input_lines("input.txt")
real_robots = get_robots_from_lines(real_input)
real_space = np.array([101, 103])

real_p100 = [get_p_after_t(r, 100, real_space) for r in real_robots]
real_safety = get_safety_factor(real_p100, real_space)
assert real_safety == 221142636
print(f"Part 1: {real_safety=}")

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

def test_count_robots_on_position(test_input):
    robots = get_robots_from_lines(test_input)
    positions = [r.p for r in robots]

    assert count_robots_on_position(positions, np.array([0, 4])) == 1
    assert count_robots_on_position(positions, np.array([2, 4])) == 1
    assert count_robots_on_position(positions, np.array([0, 0])) == 1
    assert count_robots_on_position(positions, np.array([1, 0])) == 0
    assert count_robots_on_position(positions, np.array([2, 0])) == 1
    assert count_robots_on_position(positions, np.array([3, 0])) == 2


def test_get_p_after_t():
    space = np.array([11, 7])
    r = Robot(np.array([2, 4]), np.array([2, -3]))

    assert (get_p_after_t(r, 0, space) == np.array([2, 4])).all()
    assert (get_p_after_t(r, 1, space) == np.array([4, 1])).all()
    assert (get_p_after_t(r, 2, space) == np.array([6, 5])).all()
    assert (get_p_after_t(r, 3, space) == np.array([8, 2])).all()

def test_get_p_after_t_hundred_seconds(test_input):
    space = np.array([11, 7])
    robots = get_robots_from_lines(test_input)

    p100 = [get_p_after_t(r, 100, space) for r in robots]

    assert count_robots_on_position(p100, np.array([0, 0])) == 0
    assert count_robots_on_position(p100, np.array([6, 0])) == 2
    assert count_robots_on_position(p100, np.array([9, 0])) == 1
    assert count_robots_on_position(p100, np.array([0, 2])) == 1


def test_get_safety_factor_after_t_hundred_seconds(test_input):
    space = np.array([11, 7])
    robots = get_robots_from_lines(test_input)

    p100 = [get_p_after_t(r, 100, space) for r in robots]

    assert get_safety_factor(p100, space) == 12
