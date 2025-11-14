@echo off
REM WeatherHub Installation Script

echo.
echo ====================================
echo   WeatherHub Installation Script
echo ====================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    exit /b 1
)

echo [OK] Python found
python --version

REM Upgrade pip
echo.
echo [STEP 1] Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install requirements
echo [STEP 2] Installing dependencies...
python -m pip install streamlit==1.28.1 --quiet
python -m pip install plotly==5.17.0 --quiet
python -m pip install pandas==2.0.3 --quiet
python -m pip install numpy==1.24.3 --quiet
python -m pip install requests==2.31.0 --quiet
python -m pip install pillow==10.0.0 --quiet
python -m pip install folium==0.14.0 --quiet
python -m pip install streamlit-folium==0.15.0 --quiet

echo.
echo [STEP 3] Verifying installation...
python verify_setup.py

echo.
echo ====================================
echo   Installation Complete!
echo ====================================
echo.
echo To start the application, run:
echo   streamlit run app.py
echo.
pause
