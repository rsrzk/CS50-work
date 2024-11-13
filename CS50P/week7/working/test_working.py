import pytest
from working import convert

def test_pass():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:30 AM to 12:20 PM") == "00:30 to 12:20"


def test_invalid_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:20 AM to 17:00 PM")

# def test_invalid_hour2():
#     with pytest.raises(ValueError):
#         convert("10 AM to 01 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("10 AM - 2 PM")

def test_invalid_str():
    with pytest.raises(ValueError):
        convert("cat")
