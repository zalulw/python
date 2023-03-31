from consoleIO import *
from functions import *

employe1Name: str = getNamefromConsole(1)
employe1Hours: int = getHoursfromConsole(1)
employe2Name: str = getNamefromConsole(2)
employe2Hours: int = getHoursfromConsole(2)
employe3Name: str = getNamefromConsole(3)
employe3Hours: int = getHoursfromConsole(3)
employe4Name: str = getNamefromConsole(4)
employe4Hours: int = getHoursfromConsole(4)
employe5Name: str = getNamefromConsole(5)
employe5Hours: int = getHoursfromConsole(5)

employe1Wage: int = calculateWage(employe1Hours)
employe2Wage: int = calculateWage(employe2Hours)
employe3Wage: int = calculateWage(employe3Hours)
employe4Wage: int = calculateWage(employe4Hours)
employe5Wage: int = calculateWage(employe5Hours)

printToConsole(employe1Name, employe1Hours, employe1Wage)
printToConsole(employe2Name, employe2Hours, employe2Wage)
printToConsole(employe3Name, employe3Hours, employe3Wage)
printToConsole(employe4Name, employe4Hours, employe4Wage)
printToConsole(employe5Name, employe5Hours, employe5Wage)


