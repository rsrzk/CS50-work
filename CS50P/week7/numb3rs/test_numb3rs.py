from numb3rs import validate

def test_pass():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True

def test_large():
    assert validate("275.3.6.28") == False
    assert validate("200.3.299.28") == False

def test_str():
    assert validate("cat") == False

def test_too_many():
    assert validate("220.3.6.28.6") == False

def test_too_little():
    assert validate("220.3.6") == False

def test_format():
    assert validate("220..3.6") == False
