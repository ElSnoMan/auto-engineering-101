import random


def start_game() -> dict:
    """ Start the game by initializing a new Game State object. """
    return {
        'counter': 1,
        'current_space': 0
    }


def roll_die() -> int:
    """ Roll a six-sided die and return the result. """
    roll = random.randint(0, 6)
    return roll


def advance_player(game_state: dict, roll: int) -> str:
    """ Advance the player by {roll} spaces.

    This updates the Game State object and returns a message
    that depends on if they win, overshoot, or still have spaces remaining.
    """
    GOAL = 20
    landing_space = game_state['current_space'] + roll
    message = 'Roll {0}: You rolled a {1}. '.format(game_state['counter'], roll)

    if landing_space == GOAL:
        message += f'You are on space {GOAL}. Congrats, you win!'

    if landing_space > GOAL:
        difference = landing_space - GOAL
        message += f'You lose... you overshot the goal by {difference}.'

    if landing_space < GOAL:
        remaining = GOAL - landing_space
        game_state['counter'] += 1
        game_state['current_space'] = landing_space
        message += f'You are now on space {landing_space} and have {remaining} more to go.'

    return message
