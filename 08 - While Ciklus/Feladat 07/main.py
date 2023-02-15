from os import system

biggerNumber: int = None
smallerNumber: int = None
biggerTemp: str = None
smallerTemp: str = None

while (smallerNumber == None):  
    print("kissebb szam:", end="")
    smallerTemp = input()
    break
while (biggerNumber == None or biggerNumber <= smallerNumber):
    print("nagyobb szam:", end="")
    biggerTemp = input()
    break
if (smallerTemp.isnumeric() and (biggerTemp.isnumeric())):
    biggerNumber = int(biggerTemp)
    smallerNumber = int(smallerTemp)

for i in range (biggerNumber, smallerNumber, -1):
    print(f"{i}, ", end="")