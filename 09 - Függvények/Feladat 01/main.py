from mathfunctions import *
from consoleIO import *

x: float = None
y: float = None
result: float = None


x = getNumberFromConsole()
y = getNumberFromConsole()

result = sumOfTwo(x, y)
printToConsole(x, y, result, "+")

result = multipleTwo(x, y)
printToConsole(x, y, result,  "*")

result = divideTwo(x, y)
printToConsole(x, y, result, "/")

result = substractTwo(x, y)
printToConsole(x, y, result, "-")