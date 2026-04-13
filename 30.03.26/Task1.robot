*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling windows

    Open Browser  ${url}  chrome
    Maximize Browser Window


    Click Element    id=PopUp
    Sleep    2s

    @{windows}  Get Window handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}


    Log To Console   ${titles}[-1]
    Switch Window    NEW
    Sleep    3s

    Switch Window  ${windows}[0]
    Log To Console    ${titles}[0]

    Page Should Contain    Automation Testing Practice

    Close Browser

