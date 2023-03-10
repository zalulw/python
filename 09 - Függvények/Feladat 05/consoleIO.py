def getStringfromConsoleA() -> str:
    text: str = None
    temp: str = None
    isAlpha: bool = False
    trucatedString: bool = False

    while (text == None):
        print("kerem az elso szot")
        temp = input()
        trucatedString = temp.replace(".", "").replace(".", "")
        isAlpha = trucatedString.isalpha()

        if(isAlpha):
            text = str(temp)
        
        else:
            print("nem megfelelo a megadott karakterlanc")

def getStringfromconsoleB() -> str:
    text: str = None
    temp: str = None
    isAlpha: bool = False
    trucatedString: bool = False

    while (text == None):
        print("kerem a masodik szot")
        temp = input()
        trucatedString = temp.replace(".", "").replace(".", "")
        isAlpha = trucatedString.isalpha()

        if(isAlpha):
            text = str(temp)
        
        else:
            print("nem megfelelo a megadott karakterlanc")

