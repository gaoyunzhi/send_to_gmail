from cx_Freeze import setup, Executable

setup(name = "send file",
      version = "1.1",
      description = "Description of the app here.",
      executables = [Executable("run.py", 
                                base="Win32GUI")],
      )
