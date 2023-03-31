def getNamefromConsole(index: int) -> str:
    name: str = None
    while (name == None or len(name) < 2):
        print(f"kerem a(z) {index}. dolgozo nevet: ", end="")
        name = input().strip().capitalize()
    
    return name

def getHoursfromConsole(index: int) -> int:
    workhours: int = None
    while (workhours == None):
        print(f"adja meg a(z) {index}. ledolgozott orait: ", end="")
        temp: str = input().strip()
        if (temp.isnumeric()):
            workhours = int(temp)
        
    return workhours

def printToConsole(name: str, hours: int, wage: int):
    print(f"{name} munkas {hours} orat dolgozott a heten, {wage} forintot keresett.")
    