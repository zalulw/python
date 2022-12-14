from os import system

print("milyen honap van?: ")
honap = input().strip().lower()

match honap:
    case "januar":
        print("1")

    case "februar":
        print("2")

    case "marcius":
        print("3")

    case "aprilis":
        print("4")

    case "majus":
        print("5")

    case "junius":
        print("6")

    case "julius":
        print("7")

    case "augusztus":
        print("8")

    case "szeptember":
        print("9")

    case "oktober":
        print("10")

    case "november":
        print("11")

    case "december":
        print("12")