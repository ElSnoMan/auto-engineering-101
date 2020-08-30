from chapters.ch3 import coins


def test_sum_pennies():
    total = coins.sum_pennies(user_input='50')
    assert total == 50


def test_sum_nickels():
    total = coins.sum_nickels(user_input='5')
    assert total == 25


def test_sum_dimes():
    total = coins.sum_dimes(user_input='2')
    assert total == 20


def test_sum_quarters():
    total = coins.sum_quarters(user_input='3')
    assert total == 75


def test_sum_all_coins():
    total = coins.sum_all_coins(pennies='1', nickels='1', dimes='1', quarters='1')
    assert total == 41


def test_win_with_exact_dollar():
    total = 100
    message = coins.generate_result(total)
    assert message == 'You win!'


def test_lose_with_less_than_dollar():
    total = 41
    message = coins.generate_result(total)
    assert message == 'You lose... You were under by 59 cents'


def test_lose_with_more_than_dollar():
    total = 125
    message = coins.generate_result(total)
    assert message == 'You lose... You were over by 25 cents'
