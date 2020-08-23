def convert_to_number(string):
    return int(string)


def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return 'error: invalid numbers entered'
    else:
        return x + y


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def challenge_1():
    input_1 = input('Enter a number: ')
    input_2 = input('Enter another number: ')
    num_1 = convert_to_number(input_1)
    num_2 = convert_to_number(input_2)
    total = add(num_1, num_2)
    print(total)


if __name__ == '__main__':
    challenge_1()
