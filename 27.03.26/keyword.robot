*** Setting ***
Library  SeleniumLibrary


*** Variables ***
*** Test Cases ***



*** Keywords ***
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s
    Close Browser