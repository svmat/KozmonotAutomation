
@wip
Feature: Add new product
  Background:
    Given "Cargo Bay" page loaded
    When user click "Add new product" button


  @positive @skip
  Scenario Outline: a user add new "<field>" item with data in required fields only
    When user open new  "<field>" item page
    When enter data in "<field>" required fields
    And click "Add product" "<field>" button
    Then New "<field>" item was created warning pops up

  Examples:
    |field|
    |card|


   @positive @skip
  Scenario Outline: a user add new "<field>" item with data in all fields
    When user open new  "<field>" item page
    And enter data in "<field>" required fields
    And enter data in "<field>" all non required fields
    And click "Add product" "<field>" button
    #Then New "<field>" item was created warning pops up
       Examples:
    |field|
    |card|


  @negative @skip
  Scenario Outline: a user add new "<field>" item without all required data
    When user open new  "<field>" item page
    And click "Add product" "<field>" button
    Then "This field is required" warnings pops up under all "<field>" required fields


  Examples:
    |field|
    |card|





