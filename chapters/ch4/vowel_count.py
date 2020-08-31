# 3. Refactored logic from test
def count_vowels_in_string(string):
    vowels = 'aeiou'
    count = 0
    for character in string.lower():
        if character in vowels:
            count += 1

    return count
