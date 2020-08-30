# 1. I started with my Scenarios and Examples

Feature: Count the Vowels in a String

  Scenario Outline: Count vowels in a word
    Given a {sentence}
    When I count the number of vowels in it
    Then I'll display {count}

    Examples:
      | count | sentence |
      | 5     | 'Carlos is cool' |
      | 9     | 'A cow jumped over the moon' |


  Scenario Outline: Count vowels in a sentence
    Given a {word}
    When I count the number of vowels in it
    Then I'll display {count}

    Examples:
      | count | word |
      | 0     | 'sly' |
      | 0     | '' |
      | 3     | 'Naruto' |