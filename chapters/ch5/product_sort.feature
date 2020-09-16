Feature: Sort the Product Catalog
  As a shopper
  I want different ways to sort the products
  so it's easier for me to find what I'm looking for

  Scenario: Sort by Name from Z to A
    Given the Products Page
    When I change the sort to "Name (Z to A)"
    Then the products should be in descending order

  Scenario: Sort by Name from A to Z
    Given the Products Page
    When I change the sort to "Name (A to Z)"
    Then the products should be in ascending order

  Scenario: Sort by Price from low to high
    Given the Products Page
    When I change the sort to "Price (low to high)"
    Then the products should be in ascending order, least to most expensive

  Scenario: Sort by Price from high to low
    Given the Products Page
    When I change the sort to "Price (high to low)"
    Then the products should be in descending order, most expensive to least