import pytest
from fuel import convert, gauge

def test_prop_fraction():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/10") == 0
    assert convert("8/8") == 100

def test_improp_fraction():
    with pytest.raises(ValueError):
        convert("4/3")

def test_dec():
    with pytest.raises(ValueError):
        convert("4.7/1")

def test_str():
    with pytest.raises(ValueError):
        convert("4/cat")

def test_two_slash():
    with pytest.raises(ValueError):
        convert("1/4/2")

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge_str():
    with pytest.raises(TypeError):
        gauge("test")

def test_gauge_num():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
