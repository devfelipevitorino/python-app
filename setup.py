from cx_Freeze import setup, Executable

script = "app.py"  

setup(
    name="Magnolias",
    version="2.0",
    description="",
    options={
        "build_exe": {
            "include_files": ["icon.ico"], 
        }
    },
    executables=[Executable(script, base="Win32GUI")]
)

