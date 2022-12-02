from os import system

udito = (input("Milyen uditot szeretne? [1] Coca Cola \n [2] Pepsi \n [3] Fanta \n [4] Sprite: ")).strip()

match udito:
    case "1":
        print("A valasztott udito Coca Cola")
    
    case "2":
        print("A valasztott udito Pepsi")

    case "3":
        print("A valsztott udito Fanta")

    case "4":
        print("A valasztott udito Sprite")
