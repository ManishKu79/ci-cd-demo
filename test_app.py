from app import add

def test_add():
    assert add(2, 3) == 5

def test_even():
    num = 4
    assert num % 2 == 0

def test_palindrome():
    word = "madam"
    assert word == word[::-1]