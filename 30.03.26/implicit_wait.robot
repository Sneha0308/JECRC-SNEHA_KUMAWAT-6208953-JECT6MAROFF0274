*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s

    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Close Browser





#    Get Seleniunm Implicit Wait = Return your the time of implicit wait
#    Set Selenium Implicit Wait= this keyword let you set implicit wait,usually in seconds is recommended

#     Set Browser Implicit Wait = wait for 1 browser instace
#     if there are multiple browser then itlll be confused to that browser

