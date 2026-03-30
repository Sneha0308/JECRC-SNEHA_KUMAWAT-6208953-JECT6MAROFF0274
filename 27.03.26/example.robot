*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkbox
    [Documentation]  testautomation checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

#class="form-check form-check-inline"

    Click Element    xpath=(//input[@type="checkbox"])[1]
    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s

    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s

    Unselect Checkbox  xpath=(//input[@type="checkbox"])[1]
    Sleep    2s


     Click Element   id=female
     
     Close Browser





