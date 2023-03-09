from os import system
from consoleIO import *

name: str = None

name: str = getNamefromConsole()
name = color(name)
print(f"Üdvözlöm, {name}")