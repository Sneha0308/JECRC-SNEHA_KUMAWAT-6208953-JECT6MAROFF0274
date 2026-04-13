*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window


    Click Button  xpath=//button[@onclick="jsAlert()"]
    Sleep    2s

    Handle Alert
    Sleep    2S

    Close Browser

Confirmation Alert

    Open Browser  ${url}  chrome
    Maximize Browser Window


    Click Button  xpath=//button[@onclick="jsConfirm()"]
    Sleep    2s

    Handle Alert  action=DISMISS
    Sleep    2S

    Close Browser

Prompt Alert

    Open Browser  ${url}  chrome
    Maximize Browser Window


    Click Button  xpath=//button[@onclick="jsPrompt()"]
    Sleep    2s

    Input Text Into Alert    kuch bhi  action=DISMISS
    Sleep    2S

    Close Browser