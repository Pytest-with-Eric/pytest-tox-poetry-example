import pytest
from calculator import addition, subtraction, multiplication, division


def test_addition():
    assert addition(2, 3) == 5


def test_subtraction():
    assert subtraction(2, 3) == -1


def test_multiplication():
    assert multiplication(2, 3) == 6


def test_division():
    assert division(2, 3) == 2 / 3


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(2, 0)
