from cx_Freeze import setup, Executable

script = "app.py"  

setup(
    name="Magnolias",
    version="1.0",
    description="",
    options={
        "build_exe": {
            "include_files": [], 
        }
    },
    executables=[Executable(script, base="Win32GUI")]
)

