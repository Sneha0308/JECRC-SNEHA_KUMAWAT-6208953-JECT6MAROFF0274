*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***

Handling Iframe with in an Iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Click Element    xpath=//a[@href="#Multiple"]
    Select Frame  xpath=//iframe[@src="MultipleFrames.html"]
    Select Frame    xpath=//iframe[@src="SingleFrame.html"]

    Input Text    xpath=//input[@type="text"]    Sneha
    Sleep    3s




    Close Browser