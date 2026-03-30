*** Settings ***
#Documentation   handling multiselect
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
Handling js

    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep    2s

    Execute Javascript  window.scrollTo(0,0)
    Sleep    2s

    Execute Javascript  window.scrollBy(0,500)
    Sleep    2s

    Execute Javascript  window.scrollTo(0,-200)
    Sleep    2s


    Close Browser
