from os import system

honap = (input("milyen honap van?: ")).strip().lower()

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