from Task2 import binarize
import numpy as np
import matplotlib.pyplot as plt

def test_binarize():

    M = np.array([[0.1, 0.7], [0.5, 0.6]])
    expected = np.array([[0, 1], [0, 1]])
    assert np.array_equal(binarize(M), expected)

    M = np.array([[0.1, 0.4], [0.4, 0.4]])
    expected = np.array([[0,0],[0,0]])
    assert np.array_equal(binarize(M), expected)

    M = np.array([[0.9, 0.8], [0.7, 0.7]])
    expected = np.array([[1, 1], [1, 1]])
    assert np.array_equal(binarize(M), expected)

test_binarize()
print("тесты пройдены")