def getNamefromConsole()->str:

    name: str = None

    while(name == None) or len(name) < 2:
        print("adja meg a nevet: ")
        name = str(input())

        if(len(name) < 2):
            print("nem megfelelo nev")

    return name.strip().capitalize()

def color(s: str)->str:
    value: int = len(s)
    return f"\033[38;2;{value};{value};{value}m{s}\033[0m"