from Task7 import pyramid

def test_pyramid():
    assert pyramid(14) == 3
    assert pyramid(20) == "It is impossible"
    assert pyramid(1) == 1
    assert pyramid(5) == 2
    assert pyramid(0) == "It is impossible"
    assert pyramid(-5) == "It is impossible"
    assert pyramid(55) == 5
    assert pyramid(385) == 10

test_pyramid()
print("Тесты пройдены")