from Task8 import is_balanced

def test_is_balanced():
    assert is_balanced(123803) == True
    assert is_balanced(12345) == False
    assert is_balanced(1) == True
    assert is_balanced(11) == True
    assert is_balanced(123321) == True
    assert is_balanced(123456) == False
    assert is_balanced(0) == True
    assert is_balanced(1221) == True
    assert is_balanced(1222) == False

test_is_balanced()
print("тесты пройдены")