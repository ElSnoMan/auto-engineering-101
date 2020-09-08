Feature: Google Search

  Scenario: Entering a search displays a Results Page
    Given I am on Google Search
    When I search "puppies"
    Then I see the "puppies" Results Page
