from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar2 = Jar(15)
    assert jar2.capacity == 15

def test_invalid_init():
    with pytest.raises(ValueError):
        jar = Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12 # Max capacity


def test_invalid_deposit():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(15)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0 # Min capacity

def test_invalid_withdraw():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(10)
        jar.withdraw(12)
