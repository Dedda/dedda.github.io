*** Settings ***

Library    Selenium2Library

*** Keywords ***

Open Browser To Projects Page
    Open Browser    http://dedda.github.io/projects.html    Firefox

Go To Projects Page
    Go To    http://dedda.github.io/projects.html

Check Elements
    Wait Until Page Contains Element    xpath=//h1[@id='title' and text()='Projects']
    Wait Until Page Contains Element    xpath=//div[@id='content']
    Wait Until Page Contains Element    xpath=//a[@href='https://github.com/Dedda/paintball']
    Wait Until Page Contains Element    xpath=//a[@href='https://github.com/Dedda/tibp']
    Wait Until Page Contains Element    xpath=//a[@href='https://github.com/Dedda/dedda.github.io']
    Wait Until Page Contains Element    xpath=//a[@href='https://github.com/Dedda/scheisse']

Check Links
    Go To Projects Page
    Click Element    xpath=//a[@href='https://github.com/Dedda/paintball']
    Location Should Be    https://github.com/Dedda/paintball
    Go To Projects Page
    Click Element    xpath=//a[@href='https://github.com/Dedda/tibp']
    Location Should Be    https://github.com/Dedda/tibp
    Go To Projects Page
    Click Element    xpath=//a[@href='https://github.com/Dedda/dedda.github.io']
    Location Should Be    https://github.com/Dedda/dedda.github.io
    Go To Projects Page
    Click Element    xpath=//a[@href='https://github.com/Dedda/scheisse']
    Location Should Be    https://github.com/Dedda/scheisse

*** Test Cases ***

Projects
    Open Browser To Projects Page
    Check Elements
    Check Links

Close
    Close Browser