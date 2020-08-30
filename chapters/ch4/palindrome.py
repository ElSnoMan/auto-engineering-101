def is_word_palindrome(word):
    # lowercase word(s) to ignore casing
    # and remove any whitespaces
    word = word.lower().replace(' ', '')
    reversed_word = word[::-1]
    return reversed_word == word
