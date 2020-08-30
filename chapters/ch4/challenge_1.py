# 6. Create the program
from chapters.ch4.vowel_count import count_vowels_in_string


def program():
    user_input = input('Enter a word or sentence: ')
    count = count_vowels_in_string(user_input)
    print(f'Your input has {count} vowels')


if __name__ == '__main__':
    program()
