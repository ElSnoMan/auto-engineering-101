Feature: SwagLabs Login

  Scenario: User can login with valid username and password
    Given the Login Page
    When I click LOGIN with a valid username and password
    Then I land on the Products Page


  Scenario: User can Logout
    Given I am logged in on the Products Page
    When I logout
    Then I land on the Login Page


  Scenario Outline: Cannot Login with invalid username and password
    Given the Login Page
    When I click LOGIN with an invalid {username} or {password}
    Then I see an error {message}

    Examples:
      | username | password | message |
      | 'fake'    | 'secret_sauce' | 'Username and password do not match any user in this service'
      | 'standard_user' | 'fake'   | 'Username and password do not match any user in this service'
      | ''              | 'secret_sauce'       | 'Username is required'
      | 'standard_user' | ''                   | 'Password is required'
