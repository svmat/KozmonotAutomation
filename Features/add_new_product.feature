@wip
Feature: Add new Gaming product
  As a seller, user can add new Gaming products for sale

  Background:
    Given User is on Cargo Bay page

  @positive
  Scenario Outline: User can add "<product type>" product by submitting all the required fields
    When user opens new "<product type>" product form
    And  submits all the required fields
    And  click the button "Add Product"
    Then new product is created

    Examples:
    |product type|
    |Gaming      |
    |Comics      |
    |Apparel     |

  @negative
  Scenario Outline: User can't add "<product type>" product without submitting all the required fields
    When user doesn't submit all the required fields in Add "<product type>" product pop up window
    And click the button "Add Product"
    Then warning is shown "This field is required"

    Examples:
    |product type|
    |Gaming      |
    |Comics      |
    |Apparel     |


