Feature: Identify if a word is a Palindrome

  Scenario Outline: Is it a Palindrome?
    Given a {word}
    When the word is reversed
    Then check if it {is palindrome}

    Examples:
      | is palindrome | word |
      | False     | 'Pikachu' |
      | True      | 'Race car' |
      | True      | 'madam' |
      | True      | '' |