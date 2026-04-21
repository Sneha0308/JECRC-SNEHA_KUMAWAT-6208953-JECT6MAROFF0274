*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/home_page_locators.robot

*** Keywords ***
Home page
    [Documentation]  CLICK ON ACCOUNT

    Click Element    ${account}
    Log    click on account btn

Get Success message
    ${success}  Get Text    locator
    RETURN  ${success}