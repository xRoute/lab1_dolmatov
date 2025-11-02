import numpy as np
import matplotlib.pyplot as plt
from Task1 import sum_prod

def test_sum_prod():

    X = [np.array([[1, 2], [3, 4]]), np.array([[0, 1], [1, 0]])]
    V = [np.array([[1], [1]]), np.array([[2], [3]])]
    expected = np.array([[6], [9]])
    assert np.array_equal(sum_prod(X, V), expected)

    X = [np.zeros((2, 2)), np.zeros((2, 2))]
    V = [np.array([[1], [2]]), np.array([[3], [4]])]
    expected = np.array([[0], [0]])
    assert np.array_equal(sum_prod(X, V), expected)

test_sum_prod()
print("тесты пройдены")
