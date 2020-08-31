from chapters.ch4.palindrome import is_word_palindrome


def program():
    user_input = input('Enter a word: ')
    is_palindrome = is_word_palindrome(user_input)

    if is_palindrome:
        print(f'{user_input} is a Palindrome')
    else:
        print(f'{user_input} is not a Palindrome')


if __name__ == '__main__':
    program()
