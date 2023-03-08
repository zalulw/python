def getNamefromConsole()->str:

    name: str = None

    while(name == None) or len(name) < 2:
        print("adja meg a nevet: ")
        name = str(input())

        if(len(name) < 2):
            print("nem megfelelo nev")

    return name.strip().capitalize()

def getAgefromConsole()->int:

    birthYear: int = None
    temp: str = None
    isNumber: bool = False
    trucatedString: str = False

    while(birthYear == None):
        print("adja meg a szuletesi evet: ")
        temp = input()
        trucatedString = temp.replace(".", "").replace(".", "")
        isNumber=trucatedString.isnumeric()
        
        if(isNumber):
            birthYear = int(temp)
        
        else: 
            print("nem szamot adottm meg")
        
    return birthYear
