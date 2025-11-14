"""
Setup Verification Script for WeatherHub
Run this to verify all dependencies are installed correctly
"""

import sys
import subprocess
from pathlib import Path

print("=" * 60)
print("🌤️  WeatherHub - Setup Verification Script")
print("=" * 60)

# Check Python version
print("\n✓ Checking Python version...")
py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
print(f"  Python version: {py_version}")

if sys.version_info >= (3, 8):
    print("  ✅ Python 3.8+ detected")
else:
    print("  ❌ Python 3.8+ required")
    sys.exit(1)

# Check required packages
print("\n✓ Checking required packages...")

required_packages = {
    'streamlit': '1.28.1',
    'plotly': '5.17.0',
    'pandas': '2.0.3',
    'numpy': '1.24.3',
    'requests': '2.31.0',
    'PIL': '10.0.0',
    'folium': '0.14.0',
}

missing_packages = []

for package, version in required_packages.items():
    try:
        if package == 'PIL':
            __import__('PIL')
            pkg_name = 'pillow'
        else:
            __import__(package)
            pkg_name = package
        
        print(f"  ✅ {pkg_name} installed")
    except ImportError:
        print(f"  ❌ {pkg_name} NOT found")
        missing_packages.append(pkg_name)

# Check project files
print("\n✓ Checking project files...")

project_root = Path(__file__).parent
required_files = [
    'app.py',
    'config.py',
    'weather_api.py',
    'utils.py',
    'requirements.txt',
    'README.md',
    'QUICKSTART.md',
]

missing_files = []

for file in required_files:
    file_path = project_root / file
    if file_path.exists():
        size = file_path.stat().st_size
        print(f"  ✅ {file} ({size:,} bytes)")
    else:
        print(f"  ❌ {file} NOT found")
        missing_files.append(file)

# Summary
print("\n" + "=" * 60)
print("📊 Verification Summary")
print("=" * 60)

if missing_packages or missing_files:
    print("\n⚠️  Issues found:")
    
    if missing_packages:
        print(f"\n  Missing packages ({len(missing_packages)}):")
        for pkg in missing_packages:
            print(f"    - {pkg}")
        print("\n  Run: pip install -r requirements.txt")
    
    if missing_files:
        print(f"\n  Missing files ({len(missing_files)}):")
        for file in missing_files:
            print(f"    - {file}")
else:
    print("\n✅ All checks passed!")
    print("\n🚀 You can now run:")
    print("   streamlit run app.py")

# Installation instructions if needed
if missing_packages:
    print("\n" + "=" * 60)
    print("📦 Installation Instructions")
    print("=" * 60)
    print("\n1. Create virtual environment:")
    print("   python -m venv venv")
    print("   .\\venv\\Scripts\\Activate.ps1")
    print("\n2. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("\n3. Run application:")
    print("   streamlit run app.py")

print("\n" + "=" * 60)
print("For more help, see QUICKSTART.md or README.md")
print("=" * 60)
