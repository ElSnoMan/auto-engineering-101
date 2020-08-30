from chapters.ch3 import coins


def game():
    pennies = input('Enter number of pennies: ')
    nickels = input('Enter number of nickels: ')
    dimes = input('Enter number of dimes: ')
    quarters = input('Enter number of quarters: ')
    total = coins.sum_all_coins(pennies, nickels, dimes, quarters)
    message = coins.generate_result(total)
    print(message)


if __name__ == '__main__':
    game()
