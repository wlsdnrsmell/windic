import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\jinwook\\Anaconda3\\tcl\\tcl8.6" 
os.environ['TK_LIBRARY'] = "C:\\Users\\jinwook\\Anaconda3\\tcl\\tk8.6"
setup(  name = "Dictionary",
        version = "1.0",
        description = "Dictionary",
        author = "Gin",        
        executables = [Executable("myDic.py", base="Win32GUI")])