#!/usr/bin/env python3
"""
Direct installation script for WeatherHub dependencies
Bypasses pip module loader issues
"""

import subprocess
import sys

def install_packages():
    """Install all required packages"""
    packages = [
        "streamlit==1.28.1",
        "plotly==5.17.0",
        "pandas==2.0.3",
        "numpy==1.24.3",
        "requests==2.31.0",
        "pillow==10.0.0",
        "folium==0.14.0",
        "streamlit-folium==0.15.0",
    ]
    
    print("=" * 50)
    print("WeatherHub Dependency Installation")
    print("=" * 50)
    print()
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([
                sys.executable, 
                "-m", 
                "pip", 
                "install", 
                package,
                "--no-cache-dir"
            ])
            print(f"✓ {package} installed successfully\n")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error installing {package}: {e}\n")
            continue
    
    print("=" * 50)
    print("Installation Complete!")
    print("=" * 50)
    print()
    print("To start the app:")
    print("  streamlit run app.py")
    print()

if __name__ == "__main__":
    install_packages()
