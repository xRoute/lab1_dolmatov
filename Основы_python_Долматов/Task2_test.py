from Task2 import check_individual_letter

def test_check_individual_letter():
    assert check_individual_letter("awfsdc") == True
    assert check_individual_letter("AVGSD") == True
    assert check_individual_letter("v1b4s3") == True
    assert check_individual_letter("") == True

    assert check_individual_letter("passport") == False
    assert check_individual_letter("qqwwee") == False
    assert check_individual_letter("5511") == False
    assert check_individual_letter("AabB") == False

test_check_individual_letter()
print("тесты пройдены")