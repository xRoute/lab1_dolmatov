from Task3 import count_bits

def test_count_bits():
    assert count_bits(0) == 0
    assert count_bits(1) == 1
    assert count_bits(3) == 2
    assert count_bits(7) == 3
    assert count_bits(10) == 2
    assert count_bits(15) == 4
    assert count_bits(255) == 8

test_count_bits()
print("тесты пройдены")