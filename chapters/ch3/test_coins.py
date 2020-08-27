import pytest

from chapters.ch3 import coins


def test_sum_pennies():
    total = coins.sum_pennies(user_input='50')
    assert total == 50


def test_sum_nickels():
    total = coins.sum_nickels(user_input='5')
    assert total == 25


def test_sum_dimes():
    pytest.fail()


def test_sum_quarters():
    pytest.fail()


def test_win_with_exact_dollar():
    pytest.fail()


def test_lose_with_less_than_dollar():
    pytest.fail()


def test_lose_with_more_than_dollar():
    pytest.fail()
