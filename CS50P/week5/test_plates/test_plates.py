import pytest
from plates import is_valid

def test_pass():
    assert is_valid("HOTSTF") == True
    assert is_valid("AB1234") == True

def test_not_two_letters():
    assert is_valid("A123") == False
    assert is_valid("12ABC") == False

def test_short():
    assert is_valid("AB") == True
    assert is_valid("A") == False

def test_long():
    assert is_valid("ABC12345") == False

def test_num_middle():
    assert is_valid("AB123A") == False
    assert is_valid("AB12A3") == False

def test_num_zero():
    assert is_valid("AB0123") == False

def test_punctuation():
    assert is_valid("AB123.") == False
    assert is_valid("AB-123") == False

def test_number():
    with pytest.raises(TypeError):
        is_valid(123456)
