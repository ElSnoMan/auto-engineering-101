""" I didn't do a Feature file for this challenge.

I went with a TDD approach of writing my tests firsts and then satisfying them.
I had 3 tests initially, but as I continued to code, I thought of new scenarios
and wrote the tests for them too. I arrived at 7 tests which gave me confidence
that I designed my behaviors correctly to finish the game.

Things to note:
    * I defined terms like "Game State" and "Landing Spage"
    * I started with 3 tests and quickly got to 7 after writing some code
    * I created Scenarios as examples for you as the reader, but I have more tests than Scenarios
"""

Feature: Roll the Die

    Scenario: Landing Space is under goal
        Given the player is on space 0
        And this is roll 1
        When they roll a 5
        Then the message should read, 'Roll 1: You rolled a 5. You are now on space 5 and have 15 more to go.'


    Scenario Outline: Player loses because they overshot the goal
        Given the player is on space {current space}
        And this is roll {counter}
        When they roll a {roll}
        Then the message should read, {message}

        Examples:
            | current space | counter | roll | message |
            | 18            | 4       | 3    | 'Roll 4: You rolled a 3. You lose... you overshot the goal by 1.' |
            | 19            | 5       | 2    | 'Roll 5: You rolled a 2. You lose... you overshot the goal by 1.' |


    Scenario Outline: Player wins because Landing Space is 20
        Given the player is on space {current space}
        And this is roll {counter}
        When they roll a {roll}
        Then the message should read, {message}

        Examples:
            | current space | counter | roll | message |
            | 17            | 3       | 3    | 'Roll 3: You rolled a 3. You are on space 20. Congrats, you win!' |
            | 17            | 5       | 3    | 'Roll 5: You rolled a 3. You are on space 20. Congrats, you win!' |
