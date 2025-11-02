from Task6 import number_expansion

def test_number_expasnion():
    assert number_expansion(86240) == "(2**5)(5)(7**2)(11)"
    assert number_expansion(12) == "(2**2)(3)"
    assert number_expansion(13) == "(13)"
    assert number_expansion(100) == "(2**2)(5**2)"
    assert number_expansion(1) == ""
    assert number_expansion(360) == "(2**3)(3**2)(5)"
    assert number_expansion(997) == "(997)"

test_number_expasnion()
print("тесты пройдены")
