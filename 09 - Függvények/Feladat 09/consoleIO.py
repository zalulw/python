def getAmountfromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (number == None):
        print("atvaltando ertek forintban: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number


def getCurrencyfromConsole() -> str:
    currency: str = None

    while (currency == None or currency not in ["EUR", "JPY", "USD", "CHF"]):
        print("cel valuta: ", end="")
        currency = input().upper()
    
    return currency

    
