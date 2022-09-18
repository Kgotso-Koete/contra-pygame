import sys
from cx_Freeze import setup, Executable

# with help from :https://stackoverflow.com/a/72324127/6556133
# with help from: https://stackoverflow.com/a/29671106
# with help from :https://pythonprogramming.net/converting-pygame-executable-cx_freeze/
build_exe_options = {
    "include_files": [
        "contra_pygame.py",
        "./c1_setup",
        "README.md",
    ]
}

# stop the command window from opening every time the executable is running in Windows
base = "Win32GUI" if sys.platform.lower() == "win32" else None

setup(
    name="contra_pygame",
    version="0.1",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable("contra_pygame.py", base=base)],
)  # Program name
