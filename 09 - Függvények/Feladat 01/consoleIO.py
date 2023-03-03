def getNumberFromConsole()->float:
    
    number: float = None
    temp: str = None
    isNumber: bool = False
    trucatedString: str = None

    while(number == None):
        print("adjon meg egy szamot: ",end='')
        temp = input()
        trucatedString = temp.replace(".", "").replace(".", "")
        isNumber = trucatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("nem szamot adott meg")
    
    return number

def printToConsole(a: float, b: float, result: float, operator: str)->None:
    print(f"{a} {operator} {b} = {result}")
