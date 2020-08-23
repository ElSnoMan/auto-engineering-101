from chapters.ch2.add_numbers import add, is_even, convert_to_number


def test_convert_string_to_number():
    number = convert_to_number('5')
    assert number == 5


def test_string_input():
    output = add('carlos', 2)
    assert output == 'error: invalid numbers entered'


def test_4_is_even():
    assert is_even(4)


def test_5_is_odd():
    assert is_even(5) is False


def test_adding_even_numbers_returns_even_number():
    number = add(2, 2)
    assert number == 4
    assert is_even(number)


def test_adding_negative_numbers_returns_negative_number():
    number = add(-1, -1)
    assert number == -2


def test_adding_even_and_odd_numbers_returns_positive_if_greater():
    number = add(2, -1)
    assert number == 1
