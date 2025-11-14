@echo off
REM Install dependencies and run the Streamlit app
cd /d c:\Users\prans\sem1_projectai

REM Create virtual environment if it doesn't exist
if not exist "venv_final" (
    echo Creating virtual environment...
    python -m venv venv_final
)

REM Install packages
echo Installing packages...
call venv_final\Scripts\pip.exe install -q streamlit pandas numpy plotly requests pillow

REM Check if installation was successful
if errorlevel 1 (
    echo Installation failed!
    pause
    exit /b 1
)

REM Run the app
echo Starting Streamlit app...
call venv_final\Scripts\streamlit.exe run app.py

pause
