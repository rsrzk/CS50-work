from seasons import get_mins, get_text
import pytest
from datetime import date

def test_get_mins():
    assert get_mins("1996-07-15", date(2023, 12, 27)) == 14437440

def test_get_text():
    assert get_text(14437440) == "Fourteen million, four hundred thirty-seven thousand, four hundred forty minutes"
    assert get_text(525600) == "Five hundred twenty-five thousand, six hundred minutes"

def test_invalid_format():
    with pytest.raises(ValueError):
        get_mins("1996/07/15", date(2023, 12, 27))

def test_invalid_date():
    with pytest.raises(ValueError):
        get_mins("1996/15/15", date(2023, 12, 27))

def test_invalid_date():
    with pytest.raises(TypeError):
        get_mins("1996-07-15")
