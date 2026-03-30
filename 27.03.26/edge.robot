*** Setting ***


Documentation  Opening of browser
Library  SeleniumLibrary

*** Test Cases ***
Opening Edge Browser
    [Documentation]  edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s
    Close Browser

