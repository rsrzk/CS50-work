from twttr import shorten
import pytest

def test_upper():
    assert shorten("HELLO") == "HLL"

def test_lower():
    assert shorten("twitter") == "twttr"

def test_no_vowel():
    assert shorten("CS50!") == "CS50!"

def test_number():
    with pytest.raises(TypeError):
        shorten(123)
