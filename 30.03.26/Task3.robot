Task 3

Navigate to amazon
Click on electronic in tab
Check on 'boat' checkbox
click on any product before clicking store the name of product
switch to new window
assert the product name is present in the new window
print the actual price, discounted price and the percentage
scroll to add to cart and click on the button
click on cart icon on top right corner
check if same product has been added

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Handling Add to cart

    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element  xpath=(//div[@class="nav-div"])[13]
    Sleep    2s

    Click Element  xpath=(//span[@class="a-list-item"])[26]
    Sleep    3s

    ${product_name}  Scroll Element Into View    xpath=//h2[@aria-label="Boat Wave Call 3 Smartwatch 1.83” HD Display with Animated Watch Faces; BT Calling, Functional Crown, Multiple Sports Modes, IP68, HR, SpO2 Monitor, Smart Watches for Men & Women (Bold Black)"]
    
    Log To Console    ${}
    Close Browser
