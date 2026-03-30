*** Setting ***

Documentation  Opening of browser
Library  SeleniumLibrary

*** Test Cases ***
#test cases -- all your testscript
Opening Firefox Browser
    [Documentation]  firefox browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  firefox
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
   #   work same as print

    Sleep    3s
    Close Browser

