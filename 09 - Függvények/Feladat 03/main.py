from os import system
from consoleIO import *

name: str = getNamefromConsole()
age: int = 2023 - getAgefromConsole()

print(f"{name} ön idén {age} éves")
