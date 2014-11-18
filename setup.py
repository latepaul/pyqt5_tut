import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

path_platforms = ( "C:\Python34\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll", "platforms\qwindows.dll")
egl_lib = ( "C:\Python34\Lib\site-packages\PyQt5\libEGL.dll", "libEGL.dll")

options = {
    'build_exe': {
        "includes" : [ "re", "atexit" ], "include_files" : [ path_platforms, egl_lib ],"include_msvcr": True
    }
}

executables = [
    Executable('first.py', base=base,shortcutName='HelloPaul',shortcutDir='DesktopFolder')
]

setup(name='HelloPaul',
      version='0.1',
      description="Paul's first PyQT program",
      options=options,
      executables=executables
      )