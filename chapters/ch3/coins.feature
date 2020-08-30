Feature: Change for a Dollar

  Scenario: Calculate the sum of pennies
    Given the input is '50'
    Then the sum should be 50


  Scenario: Calculate the sum of nickels
    Given the input is '5'
    Then the sum should be 25


  Scenario: Calculate the sum of dimes
    Given the input is '2'
    Then the sum should be 20


  Scenario: Calculate the sum of quarters
    Given the input is '3'
    Then the sum should be 75


  Scenario: Calculate the sum of all coins
    Given the input is '1' penny
    And '1' nickel
    And '1' dime
    And '1' quarter
    Then the sum should be 41


  Scenario Outline: Generate Game Result message
    Given the grand total is {total}
    When the result is calculated
    Then the message should be {message}

    Examples:
      | total | message |
      | 59    | 'You lose... You were under by 59 cents'|
      | 125   | 'You lose... You were over by 25 cents' |
      | 100   | 'You win!'                              |
