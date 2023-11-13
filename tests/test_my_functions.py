import pytest
import time
import source.my_functions as my_functions


def test_add():
    results = my_functions.add(2, 5)
    assert results == 7


def test_divide():
    results = my_functions.divide(10, 5)
    assert results == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    results = my_functions.divide(10, 5)
    assert results == 2


@pytest.mark.skip(reason="feature not introduced")
def test_multiply():
    results = my_functions.multiply(10, 5)
    assert results == 50


@pytest.mark.xfail(reason="we know we cannot divide by zero")
def test_divide_by_zero_broken():
    my_functions.divide(4, 0)
