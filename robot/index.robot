*** Settings ***

Library    Selenium2Library

*** Keywords ***

Open Browser To Index Page
    Open Browser    http://dedda.github.io/    Firefox

Go To Index Page
    Go To    http://dedda.github.io/

Check Links
    Go To Index Page
    Click Element    xpath=//div[@class='content-unit']/ul/li/a[@href='projects.html']
    Location Should Be    http://dedda.github.io/projects.html

*** Test Cases ***

Index
    Open Browser To Index Page
    Wait Until Page Contains Element    xpath=//h1[@id='title']
    Wait Until Page Contains Element    xpath=//div[@id='content']
    Wait Until Page Contains Element    xpath=//div[@class='content-unit']
    Wait Until Page Contains Element    xpath=//div[@class='content-unit']/ul/li/a[@href='projects.html']
    Check Links

Close
    Close Browser