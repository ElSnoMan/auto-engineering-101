import pytest

from chapters.ch4.palindrome import is_word_palindrome

examples = [
    (False, 'Pikachu'),
    (True, 'Race car'),
    (True, 'madam'),
    (True, '')
]


@pytest.mark.parametrize('is_palindrome, word', examples)
def test_is_palindrome(is_palindrome, word):
    output = is_word_palindrome(word)
    assert is_palindrome == output
