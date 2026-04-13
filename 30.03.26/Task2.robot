#id="alertBtn"

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window


    Click Button  id=alertBtn
    Sleep    2s

    Handle Alert
    Sleep    2S

    Close Browser

Confirmation alert-accepting
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    id=confirmBtn
    Click Button    id=confirmBtn
    Sleep    2s
    Handle Alert
    Sleep    3s
    Page Should Contain    You pressed OK!
    ${msg}  Get Text    id=demo
    Log To Console    ${msg}
    Close Browser




Prompt alert-cancelling
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    id=promptBtn
    Click Button    id=promptBtn
    Sleep    2s
    ${text}=  Set Variable  Sneha
    Input Text Into Alert    ${text}  action=DISMISS
    Page Should Contain    cancelled
    ${msg}  Get Text    id=demo
    Log To Console    ${msg}
    Close Browser