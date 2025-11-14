# 🔧 WeatherHub - Python Installation Fix Guide

## Issue Summary

Your Python 3.14.0 installation is corrupted with a missing `pip._vendor.rich` module. This is a known issue with Python 3.14 (beta version).

**Solution: Reinstall Python 3.11 or 3.12**

---

## ✅ Quick Fix (5 minutes)

### Step 1: Remove Current Python Installation

**Option A: Using Windows Settings (GUI)**
1. Open Settings → Apps → Installed apps
2. Search for "Python"
3. Click on "Python 3.14" → Uninstall
4. Click "Uninstall" in the dialog

**Option B: Using Command Line**
```powershell
winget uninstall Python.Python.3.14
```

### Step 2: Install Python 3.12 (Stable Version)

**Option A: Download from Website**
1. Visit: https://www.python.org/downloads/
2. Click "Download Python 3.12.X" (Latest 3.12 version)
3. Run the installer
4. ⚠️ **IMPORTANT**: Check "Add Python to PATH" ✓
5. Click "Install Now"

**Option B: Using Windows Package Manager**
```powershell
winget install Python.Python.3.12
```

### Step 3: Verify Installation

```powershell
python --version
```

Should show: `Python 3.12.X` (not 3.14)

### Step 4: Install Dependencies

```powershell
cd c:\Users\prans\sem1_projectai
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 5: Run the Application

```powershell
streamlit run app.py
```

**Browser will open automatically!** 🎉

---

## 📋 Detailed Step-by-Step Guide

### STEP 1: Uninstall Python 3.14

**PowerShell as Administrator:**
```powershell
# Using winget
winget uninstall Python.Python.3.14

# Or remove files manually
Remove-Item "C:\Users\$env:USERNAME\AppData\Local\Python\pythoncore-3.14-64" -Recurse -Force
```

**Via GUI:**
1. Settings → Apps → Installed apps
2. Search "Python"
3. Click "Python 3.14.0"
4. Click "Uninstall"
5. Confirm removal

### STEP 2: Download Python 3.12

Go to: https://www.python.org/downloads/

**Download the latest 3.12 version:**
- Look for "Latest Python 3.12 Release"
- Click the download button
- Choose "Windows installer (64-bit)" for your system

### STEP 3: Install Python 3.12

1. Run the downloaded `.exe` file
2. **IMPORTANT**: Check "Add Python to PATH" ✓
3. Click "Install Now"
4. Wait for installation to complete
5. Click "Close"

### STEP 4: Verify Python Installation

Open PowerShell and type:
```powershell
python --version
```

Expected output: `Python 3.12.X` (or similar 3.12 version)

If it shows 3.14, restart your computer and try again.

### STEP 5: Navigate to Project

```powershell
cd c:\Users\prans\sem1_projectai
```

### STEP 6: Upgrade Pip

```powershell
python -m pip install --upgrade pip
```

Expected: Shows "Successfully installed pip-24.X.X" or similar

### STEP 7: Install All Dependencies

```powershell
python -m pip install -r requirements.txt
```

Expected output (for each package):
```
Successfully installed streamlit-1.28.1
Successfully installed plotly-5.17.0
Successfully installed pandas-2.0.3
...etc
```

### STEP 8: Run the Application

```powershell
streamlit run app.py
```

**Browser automatically opens to `http://localhost:8501`** 🌤️

---

## ❌ Troubleshooting

### Problem: "python: The term 'python' is not recognized"

**Cause**: Python not in PATH

**Solution**:
1. Reinstall Python (check "Add to PATH" option)
2. Restart PowerShell/Computer
3. Or use full path: `C:\Users\prans\AppData\Local\Programs\Python\Python312\python.exe`

### Problem: "pip._vendor.rich" module not found

**Cause**: Corrupted pip installation

**Solution**:
```powershell
# Uninstall Python 3.14
winget uninstall Python.Python.3.14

# Install Python 3.12
winget install Python.Python.3.12

# Verify
python --version
```

### Problem: "No module named 'streamlit'"

**Cause**: Dependencies not installed

**Solution**:
```powershell
python -m pip install -r requirements.txt
```

### Problem: Port 8501 already in use

**Solution**:
```powershell
# Use different port
streamlit run app.py --server.port 8502
```

---

## 📊 Python Version Recommendations

| Version | Status | Recommendation |
|---------|--------|-----------------|
| 3.8 | Old | ⚠️ Works but outdated |
| 3.9 | Old | ⚠️ Works but outdated |
| 3.10 | Stable | ✅ Good choice |
| 3.11 | Stable | ✅ **Recommended** |
| 3.12 | Stable | ✅ **Recommended** |
| 3.13 | New | ⚠️ Some compatibility issues |
| 3.14 | Beta | ❌ **Not stable** - Has bugs |

**Use 3.11 or 3.12** for best compatibility!

---

## ✅ Verification Checklist

After installation, verify everything works:

```powershell
# 1. Check Python version
python --version
# Expected: Python 3.12.X or 3.11.X

# 2. Check pip version
python -m pip --version
# Expected: pip X.X.X from ... (not error)

# 3. Check packages installed
python -m pip list
# Should show: streamlit, plotly, pandas, numpy, requests, pillow, folium

# 4. Navigate to project
cd c:\Users\prans\sem1_projectai

# 5. Run the application
streamlit run app.py
# Should open browser automatically
```

---

## 🚀 Alternative: Use Virtual Environment

If you want to keep multiple Python versions:

```powershell
# Navigate to project
cd c:\Users\prans\sem1_projectai

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install -r requirements.txt

# Run app
streamlit run app.py

# To deactivate later
deactivate
```

---

## 📞 Support Resources

| Issue | Resource |
|-------|----------|
| Python installation | https://www.python.org/downloads/ |
| Pip documentation | https://pip.pypa.io/ |
| Streamlit help | https://docs.streamlit.io |
| Project files | c:\Users\prans\sem1_projectai\ |

---

## ✨ Once Installation is Fixed

Your application will have:

- ✅ Beautiful glassmorphism UI
- ✅ Responsive design for all devices
- ✅ Interactive weather charts
- ✅ Global weather map
- ✅ All 5 pages (Dashboard, Location, Analytics, Settings, About)
- ✅ Professional documentation

---

## 🎯 Final Commands

After fixing Python, use these commands:

```powershell
# 1. Navigate to project
cd c:\Users\prans\sem1_projectai

# 2. Install dependencies (one time)
python -m pip install -r requirements.txt

# 3. Run the app (every time you want to use it)
streamlit run app.py

# 4. Stop the app
Ctrl + C (in PowerShell)
```

---

**All your application files are ready and waiting!**

Just fix Python and run: `streamlit run app.py`

🌤️ **Enjoy WeatherHub!** 🌈
