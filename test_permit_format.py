from permit_numbers import permit_number_checker

def test_pytest():
    assert 1+1 == 2

def test_permit_number_is_given_unhappy():
    assert permit_number_checker("") == False

def test_permit_number_is_8_characters_unhappy():
    assert permit_number_checker("1234567") == False
    assert permit_number_checker("123456789") == False

def test_permit_number_is_correct_format_unhappy():
    assert permit_number_checker("12345678") == False

def test_permit_number_is_correct_format_happy():
    assert permit_number_checker("ab1234cd") == True



