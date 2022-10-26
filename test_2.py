import pytest


def test_method1():
    x = 0
    y = 1
    assert x == y
    

def test_method2():
    a = 2
    b = 5
    assert a + 3 == b
    
# to run individual tests use 'pytest test_1.py::test_method1' or 'pytest test_2.py::test_method1' command
