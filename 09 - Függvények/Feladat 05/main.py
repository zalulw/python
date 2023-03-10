from os import system
from consoleIO import *
from mathfunctions import *

text1: str = getStringfromConsoleA()
text2: str = getStringfromconsoleB()
count: int = calculateSameLetters()

print(f"{text1}, {text2} -> {count}")