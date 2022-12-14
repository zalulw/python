from os import system

print("hanyadik napja van a hetnek: " )
day = input().strip()

match day:
    case "1":
        print("hetfo")
    
    case "2":
        print("kedd")

    case "3":
        print("szerda")        

    case "4":
        print("csutortok")

    case "5":
        print("pentek")

    case "6":
        print("szombat")

    case "7":
        print("vasarnap")