from os import system
from consoleIO import *
from mathfunctions import *

print("kerem az elso szot")
text1: str = getStringfromConsole()
print("kerem a masodik szot")
text2: str = getStringfromConsole()

intersection: int = calculateSameLetters(text1, text2)

print(f"{text1}, {text2} -> {intersection}")