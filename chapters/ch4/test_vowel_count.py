# 2. After describing my Scenarios in vowels.feature,
#    I wrote this spec with the logic and mocked user_input.
#    Then I refactored because now I knew what I needed for the rest
#    of the examples.
def test_sentence():
    user_input = 'Carlos is cool'
    vowels = 'aeiou'
    count = 0
    for character in user_input.lower():
        if character in vowels:
            count += 1
    assert count == 5


# 4. import and update the test
from chapters.ch4.vowel_count import count_vowels_in_string


def test_vowel_count_with_sentence():
    user_input = 'Carlos is cool'
    count = count_vowels_in_string(user_input)
    assert count == 5


def test_vowel_count_with_uppercase_vowels():
    user_input = 'A cow jumped over the moon'
    count = count_vowels_in_string(user_input)
    assert count == 9


# 5. Use pytest's parametrize feature to pass in a list of examples
#    to my test - just like the Scenario Outline.
import pytest

examples = [
    ('sly', 0),    # word with no vowels
    ('', 0),       # empty word
    ('Naruto', 3)  # word with vowels
]


@pytest.mark.parametrize('word, count', examples)
def test_vowel_count_with_single_words(word, count):
    number_of_vowels = count_vowels_in_string(word)
    assert count == number_of_vowels
