from cx_Freeze import setup, Executable

setup(
    name="Chain Renamer",
    version="0.9",
    description="MyEXE",
    executables=[Executable("rename.py", base="Win32GUI")],
    )