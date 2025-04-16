Feature: Login Feature

Scenario: Success Login with correct credential
    Given I am on the homepage
    When I fill my credential
    And I click login
    Then I should be logged in


Scenario: Failed Login with incorrect credential
    Given I am on the homepage
    When I fill my credential with wrong password
    And I click login
    Then I should see an error message