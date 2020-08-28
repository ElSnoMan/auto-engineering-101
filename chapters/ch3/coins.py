def sum_pennies(user_input):
    pennies = int(user_input)
    return pennies


def sum_nickels(user_input):
    nickels = int(user_input) * 5
    return nickels


def sum_dimes(user_input):
    dimes = int(user_input) * 10
    return dimes


def sum_quarters(user_input):
    quarters = int(user_input) * 25
    return quarters


def sum_all_coins(pennies, nickels, dimes, quarters):
    return sum([
        sum_pennies(pennies),
        sum_nickels(nickels),
        sum_dimes(dimes),
        sum_quarters(quarters)
    ])
