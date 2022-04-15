from cx_Freeze import setup, Executable
base = None
executables = [Executable("scriptV1.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name="ScriptWebPython",
    options=options,
    version="1.3",
    description='ScriptWebPython',
    executables=executables
)

executables.append(Executable(
    'scriptV1.exe',
    targetName='scriptV1',
    base='Win32GUI',
    icon='icon.png',
    shortcutDir='DesktopFolder',
    shortcutName='scriptV1.exe'
))
# End of file

# python setup.py build