def getTemperatureFromConsole()->int:

    celsius: int = None
    temp: str = None
    isNumber: bool = False
    trucatedString: str = False

    while(celsius == None):
        print("adja meg a homersekletet celsiusban: ")
        temp = input()
        trucatedString = temp.replace(".", "").replace(".", "")
        isNumber=trucatedString.isnumeric()
        
        if(isNumber):
            celsius = int(temp)
        
        else: 
            print("nem szamot adottm meg")
        
    return celsius