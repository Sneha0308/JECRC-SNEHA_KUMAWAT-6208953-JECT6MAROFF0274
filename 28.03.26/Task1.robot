*** Settings ***
Documentation   handling multiselect
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling dropdown

    Open Browser  ${url}  chrome
    Maximize Browser Window
    
#    Click Element    id=colors
#    Sleep    2s
    Scroll Element Into View   xpath=//label[text()="Colors:"]
    Page Should Contain List    id=colors
    
    ${options}=  Get List Items    id=colors
    Log To Console    ${options}

    Select From List By Index  id=colors  4
    Select From List By Index  id=colors  3


    @{select_options}=  Get Selected List Labels    id=colors
    Log To Console    ${select_options}

    Sleep    3s
    Close Browser
    