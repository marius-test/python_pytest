import pytest


def func(x):
    return x + 1


def test_method():
    assert func(2) == 3


# to run the all tests in a module execute the "pytest test1.py" command in the Terminal
