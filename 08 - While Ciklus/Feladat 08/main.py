from os import system

valasztas: int = None
temp: str = None

print("1 - 7UP \n 2 - Kinley Gyömbér \n 3 - Fanta \n 4 - Sió Barack \n 5 - Kubu")

while (valasztas == None or not (valasztas > 0 and valasztas <= 5)):
    print("ital:")
    temp = input()

    if (temp.isnumeric()):
        valasztas = int(temp)

match valasztas: 
    case 1:
        drink ="7UP"
    case 2:
        drink ="Kinley"
    case 3:
        drink ="Fanta"
    case 4:
        drink ="Sió barack"
    case 5:
        drink ="kubu"

print(f"A választott ital a {drink}")