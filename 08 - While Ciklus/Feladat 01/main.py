from os import system
system('cls')

number: float = None
temp: str = None
isNumber: bool = False
trucatedString: str = None

while(number == None or (number < 0 or number > 9)):
    print("adjon meg egy szamot: ",end='')
    temp = input()
    trucatedString = temp.replace(".", "").replace(".", "")
    isNumber = trucatedString.isnumeric()

    if (isNumber):
        number = float(temp)
    else:
        print("nem szamot adott meg")
    