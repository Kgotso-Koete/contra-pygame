import sys
from cx_Freeze import setup, Executable
from settings import *

# with help from :https://stackoverflow.com/a/72324127/6556133
# with help from: https://stackoverflow.com/a/29671106
# with help from :https://pythonprogramming.net/converting-pygame-executable-cx_freeze/
include_files = [
    "main.py",
    "settings.py",
    "README.md",
    "./app",
    "./assets",
]
targetName = "contra"
name = "main.py"
script = "main.py"
description = "Contra clone"
options = {"build_exe": {"include_files": include_files, "path": sys.path}}


# stop the command window from opening every time the executable is running in Windows
base = "Win32GUI" if sys.platform.lower() == "win32" else None
executable = Executable(script="main.py", targetName=targetName, base=base)
executables = [executable]


setup(name=name, version="0.1", description=description, options=options, executables=executables)
