import os
import platform
import subprocess

def build():
    system = platform.system()
    
    if system == "Darwin":  # macOS
        name = "NewYearTree-macOS"
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            f"--name={name}",
            "main.py"
        ]
    elif system == "Windows":
        name = "NewYearTree-Windows"
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            f"--name={name}",
            "main.py"
        ]
    else:  # Linux
        name = "NewYearTree-Linux"
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            f"--name={name}",
            "main.py"
        ]
    
    print(f"Building for {system}...")
    subprocess.run(cmd)
    print(f"\nBuild complete! Check the 'dist' folder for {name}")

if __name__ == "__main__":
    build()