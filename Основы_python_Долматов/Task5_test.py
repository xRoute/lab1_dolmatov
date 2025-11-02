from Task5 import mse

def test_mse():
    assert mse([1, 2, 3], [1, 2, 3]) == 0
    assert mse([1, 2, 3], [0, 0, 0]) == 14/3
    assert mse([1, 2, 3], [3, 2, 1]) == 8/3
    assert mse([0, 0, 0], [1, 1, 1]) == 1
    assert mse([5, 5, 5], [2, 2, 2]) == 9

test_mse()
print("тесты пройдены")