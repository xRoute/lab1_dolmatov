from Task3 import unique_rows, unique_columns
import numpy as np
import matplotlib.pyplot as plt

def test_unique():

    mat = np.array([[1,2,2],[3,3,4]])
    expected_rows = [np.array([1, 2]), np.array([3, 4])]
    rows_result = unique_rows(mat)
    for r1, r2 in zip(rows_result, expected_rows):
        assert np.array_equal(r1, r2)
    expected_cols = [np.array([1,3]), np.array([2,3]), np.array([2,4])]
    cols_result = unique_columns(mat)
    for c1, c2 in zip(cols_result, expected_cols):
        assert np.array_equal(c1, c2)

    mat2 = np.array([[5, 5, 5], [5, 5, 5]])
    expected_rows2 = [np.array([5]), np.array([5])]
    expected_cols2 = [np.array([5]), np.array([5]), np.array([5])]
    for r1, r2 in zip(unique_rows(mat2), expected_rows2):
        assert np.array_equal(r1, r2)
    for c1, c2 in zip(unique_columns(mat2), expected_cols2):
        assert np.array_equal(c1, c2)

test_unique()
print("тесты пройдены")
