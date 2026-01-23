@echo off
set "base_dest=C:\Users\%USERNAME%\.gemini\skills"

REM Check if parameter is provided
if "%~1"=="" (
    echo Usage: %~nx0 "Source_Directory_Path"
    echo Example: %~nx0 "docx"
    pause
    exit /b 1
)

set "source=%~1"
REM Get source directory name
set "folder_name=%~nx1"

REM Check if source directory exists
if not exist "%source%" (
    echo Error: Source directory "%source%" does not exist.
    pause
    exit /b 1
)

REM Set final destination path to base_dest\folder_name
set "destination=%base_dest%\%folder_name%"

echo Installing skill from "%source%" to "%destination%"...

if not exist "%destination%" (
    mkdir "%destination%"
)

REM Execute copy
xcopy "%source%\*" "%destination%\" /E /I /Y /H

echo Installation completed.
