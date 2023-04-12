from random import *
from consoleIO import *
from function import *

num1: int = getNumberfromConsole(0, 9)
num2: int = getNumberfromConsole(40, 50)

randNum: int = randint(num1, num2) 

game(randNum)

