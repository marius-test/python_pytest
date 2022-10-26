import pytest


@pytest.mark.test1
def test_method1():
    x = 0
    y = 1
    assert x > y
    

@pytest.mark.test2
def test_method2():
    a = "Hello"
    b = " World!"
    assert a + b == "Hello World!"
    
    
# to run marked tests use the 'pytest -v -m test1' or 'pytest -v -m test2' command
