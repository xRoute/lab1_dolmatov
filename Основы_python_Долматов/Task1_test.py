from Task1 import count_vowels

def test_count_vowels():
    assert count_vowels("right") == 1
    assert count_vowels("RIGHT") == 1
    assert count_vowels("why") == 0
    assert count_vowels("faeokiu") == 5
    assert count_vowels("manual") == 3
    assert count_vowels("") == 0
    assert count_vowels("DataScience") == 5

test_count_vowels()
print("Тесты пройдены")