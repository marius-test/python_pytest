import pytest


@pytest.mark.parametrize("x, y, z", [(1, 2, 3), (4, 5, 6)])
def test_method(x, y, z):
    assert x + y == z


# The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function.