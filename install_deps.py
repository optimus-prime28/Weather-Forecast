#!/usr/bin/env python3
"""
Direct pip installer - bypass PowerShell issues
"""
import subprocess
import sys
import os

def install_packages():
    """Install required packages using subprocess"""
    python_exe = sys.executable
    packages = [
        'streamlit==1.28.1',
        'pandas==2.0.3',
        'numpy==1.24.3',
        'plotly==5.17.0',
        'requests==2.31.0',
        'pillow==10.0.0'
    ]
    
    print(f"Using Python: {python_exe}")
    print(f"Python version: {sys.version}\n")
    
    for package in packages:
        print(f"[*] Installing {package}...")
        try:
            result = subprocess.run(
                [python_exe, '-m', 'pip', 'install', package, '-q'],
                capture_output=True,
                timeout=120,
                check=False
            )
            if result.returncode == 0:
                print(f"[✓] {package} installed successfully")
            else:
                print(f"[!] {package} installation had issues")
                if result.stderr:
                    print(f"    Error: {result.stderr.decode()[:100]}")
        except subprocess.TimeoutExpired:
            print(f"[!] {package} installation timed out")
        except Exception as e:
            print(f"[!] {package} error: {e}")
    
    print("\n[*] Installation complete!")
    print("[*] Running: streamlit run app.py\n")
    
    # Run streamlit
    try:
        subprocess.run([python_exe, '-m', 'streamlit', 'run', 'app.py'], check=False)
    except Exception as e:
        print(f"Error running streamlit: {e}")

if __name__ == '__main__':
    os.chdir(r'c:\Users\prans\sem1_projectai')
    install_packages()
