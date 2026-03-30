*** Settings ***
Documentation   handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling dropdown

    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element   xpath=//a[text()="Dropdown"]

    Page Should Contain List    id=dropdown

#    assigining a value
    ${options}=  Get List Items    id=dropdown

    Log To Console    ${options}

    Select From List By Label  id=dropdown  Option 1

    ${select_options}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_options}

    Sleep    3s
    Close Browser