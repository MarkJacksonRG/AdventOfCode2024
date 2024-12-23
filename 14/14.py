import pytest

import numpy as np

from helpers.helpers import get_input_lines


class Robot:
    pos: np.array
    direction: np.array


@pytest.fixture
def test_input():
    return get_input_lines("test.txt")

def test_get_input_lines(test_input):
    assert len(test_input) == 12
