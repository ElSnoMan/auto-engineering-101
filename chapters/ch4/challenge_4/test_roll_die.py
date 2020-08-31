""" Challenge 4 - Roll the Die

Objective:
    Travel the entire game board of 20 spaces within 5 die rolls.

Rules:
    * Roll the die for the user (a randomly generated number between 1 and 6)
    * Advance the user that many spaces on the game board
    * After each roll, tell the user which space they are on and how many spaces they need to go to win
    * Repeat this 4 additional times for 5 rolls in total

How to Win or Lose:
    * If the user gets to 20 before 5 rolls, end the game - they won!
    * If they are greater than or less than 20 spaces - they lose!

Remember, there are only 20 spaces on the board, so a message like:

> “You advanced to space 22” is a BUG!

Example Output:
    Roll 1: You rolled a 3. You are now on space 3 and have 17 more to go.
"""
from chapters.ch4.challenge_4 import game


# Leave this test here as an example
def test_rolling_a_die():
    """ Not a very good test because it's not deterministic. """
    roll = game.roll_die()
    assert roll in range(0, 7)


def test_initial_game_state_object():
    game_state = game.start_game()
    assert game_state == {'counter': 1, 'current_space': 0}


def test_player_under_goal():
    roll = 5
    game_state = {'counter': 1, 'current_space': 0}

    message = game.advance_player(game_state, roll)
    assert message == 'Roll 1: You rolled a 5. You are now on space 5 and have 15 more to go.'


def test_player_overshot_goal_before_5th_roll():
    roll = 3
    game_state = {'counter': 4, 'current_space': 18}

    message = game.advance_player(game_state, roll)
    assert message == 'Roll 4: You rolled a 3. You lose... you overshot the goal by 1.'


def test_player_overshot_goal_on_5th_roll():
    roll = 2
    game_state = {'counter': 5, 'current_space': 19}

    message = game.advance_player(game_state, roll)
    assert message == 'Roll 5: You rolled a 2. You lose... you overshot the goal by 1.'


def test_player_wins_before_5th_roll():
    roll = 3
    game_state = {'counter': 3, 'current_space': 17}

    message = game.advance_player(game_state, roll)
    assert message == 'Roll 3: You rolled a 3. You are on space 20. Congrats, you win!'


def test_player_wins_on_5th_roll():
    roll = 3
    game_state = {'counter': 5, 'current_space': 17}

    message = game.advance_player(game_state, roll)
    assert message == 'Roll 5: You rolled a 3. You are on space 20. Congrats, you win!'
