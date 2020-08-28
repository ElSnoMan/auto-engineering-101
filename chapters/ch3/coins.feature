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