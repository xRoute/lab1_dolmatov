import numpy as np
import matplotlib.pyplot as plt
from Task5 import chess

def test_chess():
    expected = np.array([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ])
    assert np.array_equal(chess(3, 3, 1, 0), expected)

    expected = np.array([
        [5, 7, 5, 7],
        [7, 5, 7, 5]
    ])
    assert np.array_equal(chess(2, 4, 5, 7), expected)

    expected = np.array([[9]])
    assert np.array_equal(chess(1, 1, 9, 0), expected)

    expected = np.array([
        [2, 3, 2],
        [3, 2, 3]
    ])
    assert np.array_equal(chess(2, 3, 2, 3), expected)

test_chess()
print("тесты пройдены")