from os import system

biggerNumber: int = None
smallerNumber: int = None
biggerTemp: str = None
smallerTemp: str = None

while ((smallerNumber == None or biggerNumber == None) or biggerNumber <= smallerNumber):   #kulon kell bekerni a 2 szamot
    print("kissebb szam:", end="")
    smallerTemp = input()

    print("nagyobb szam:", end="")
    biggerTemp = input()

    if (smallerTemp.isnumeric() and (biggerTemp.isnumeric())):
        biggerNumber = int(biggerTemp)
        smallerNumber = int(smallerTemp)

for i in range (biggerNumber, smallerNumber, -1):
    print(f"{i}, ", end="")