# WeatherHub Installation Script (PowerShell)
# Run: powershell -ExecutionPolicy Bypass -File install.ps1

Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  WeatherHub Installation Script" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[STEP 1] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Upgrade pip
Write-Host ""
Write-Host "[STEP 2] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip -q
Write-Host "[OK] Pip upgraded" -ForegroundColor Green

# Install individual packages
Write-Host ""
Write-Host "[STEP 3] Installing dependencies..." -ForegroundColor Yellow

$packages = @(
    "streamlit==1.28.1",
    "plotly==5.17.0",
    "pandas==2.0.3",
    "numpy==1.24.3",
    "requests==2.31.0",
    "pillow==10.0.0",
    "folium==0.14.0",
    "streamlit-folium==0.15.0"
)

foreach ($package in $packages) {
    Write-Host "  Installing $package..." -ForegroundColor Gray
    python -m pip install $package -q
    Write-Host "  [OK] $package installed" -ForegroundColor Green
}

# Verify installation
Write-Host ""
Write-Host "[STEP 4] Verifying installation..." -ForegroundColor Yellow
python verify_setup.py

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  Installation Complete!" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the application, run:" -ForegroundColor Yellow
Write-Host "  streamlit run app.py" -ForegroundColor Cyan
Write-Host ""
