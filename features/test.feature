Feature: Selenium Runs

Scenario: Search query with common terms in PPS
	Given I have a bookable directory
	When I enter fever in the PPS 
	Then I see child fever in the search results 