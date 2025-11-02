from Task4 import magic

def test_magic():

    assert magic(39) == 3
    assert magic(4) == 0
    assert magic(999) == 4
    assert magic(25) == 2
    assert magic(77) == 4
    assert magic(10) == 1

test_magic()
print("тесты пройдены")