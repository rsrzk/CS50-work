from um import count
import pytest

def test_count():
    assert count("Um, I am um not sure but this is yummy wumbo um: um. Hum") == 4
    assert count("UM") == 1

def test_none():
    assert count("umm") == 0
    assert count("Yummy") == 0
    assert count(" rum ") == 0

def test_punctuation():
    assert count("!um- but,um we um. (um)") == 4

def test_invalid_num():
    with pytest.raises(TypeError):
        count(42)
