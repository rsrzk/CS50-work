from bank import value
import pytest

def test_h():
    assert value("h") == 20
    assert value("HI") == 20
    assert value("  hey") == 20

def test_hello():
    assert value("HELLO, world") == 0
    assert value("  heLLo David") == 0

def test_no_greet():
    assert value("") == 100
    assert value("123") == 100
    assert value("What's up?") == 100

def test_number():
    with pytest.raises(AttributeError):
        value(123)
