import pytest


@pytest.fixture
def list1():
    list1_= [5, 6, 7]
    return list1_


# to skip a test use the following
@pytest.mark.skip
def test_1(list1):
    x = 3
    assert list1[0] == x
    
    
def test_2(list1):
    y = 6
    assert list1[1] == y
    
    
def test_3(list1):
    z = 9
    assert list1[2] == z


# Pytest fixtures are functions that can be used to manage our apps states and dependencies,
# they can provide data for testing and a wide range of value types when explicitly called by our testing software.
