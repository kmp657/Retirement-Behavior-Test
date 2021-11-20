@retirement-calculator
Feature: Retirement Age Calculator
  As a web surfer,
  I want to search Google for the full retirement age calculator,
  So I can determine my full retirement age, and the month and year I become eligible to retire

  Scenario: Simple Google Search
    Given a web browser is on the Google page
    When the search phrase Retirement Age calculator is entered
    Then results for Retirement Age calculator are shown

  Scenario: Open Retirement Age calculator
    Given a web browser is on the Retirement Age calculator
    When the user opens the calculator
    Then can enter their year of birth

  Scenario: Enter year of birth in calculator
    Given Retirement Age calculator asks user to enter year of birth
    When the user enters their year of birth
    Then the Retirement Age calculator asks user to enter month of birth

  Scenario: Enter the month of birth in calculator
    Given Retirement Age calculator asks user to enter month of birth
    When the user enters their month of birth
    Then the Retirement Age calculator displays to the user what their full retirement age will be
    And the Retirement Age calculator will show the user the month and year can retire

  Scenario: User exits Retirement Age calculator
    Given the user has completed their search
    When the calculator returns Enter the year of birth or 1 to exit
    Then user enters 1 to exit

  Scenario Outline: Add user year of birth to calculator
    Given the user year of birth is "<initial>"
    When user enters birth month as "<some>"
    Then the full retirement age is "<age>"and 0 months
    And will be able to retire in January of 2032

    Examples: Retirement Age
    | initial | some | age
    | 1965     | 1   | 67

  Scenario Outline: Add user year of birth to calculator
    Given the user year of birth is "<initial>"
    When user enters birth month as "<some>"
    Then the full retirement age is "<age>"and 0 months
    And will be able to retire in August of 1983

   Examples: Retirement Age
    | initial | some | age
    | 1918     | 8   | 65

  Scenario Outline: Add user year of birth to calculator
    Given the user year of birth is "<initial>"
    When user enters birth month as "<some>"
    Then the full retirement age is "<age>" and 0 months
    And will be able to retire in May of 2048

     Examples: Retirement Age
    | initial | some | age
    | 1984     | 5   | 67

  Scenario: Add user year of birth before 1900
    Given the user was born before 1899
    When year of birth is entered
    Then system returns invalid year range

  Scenario: Add user year of birth after 2021
     Given the user was born after 2021
     When year of birth is entered
     Then system returns invalid year range


