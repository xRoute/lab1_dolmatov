import numpy as np
import matplotlib.pyplot as plt
from Task8 import one_hot_encode

def test_one_hot():
    labels = [0, 2, 3, 0]
    expected = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ])
    assert np.array_equal(one_hot_encode(labels), expected)

    labels = [0, 0, 0]
    expected = np.array([
        [1],
        [1],
        [1]
    ])
    assert np.array_equal(one_hot_encode(labels), expected)

    labels = [1, 0, 2]
    expected = np.array([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ])
    assert np.array_equal(one_hot_encode(labels), expected)

test_one_hot()
print("тесты пройдены")