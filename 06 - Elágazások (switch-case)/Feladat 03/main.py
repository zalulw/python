from os import system

print("Milyen uditot szeretne? [1] Coca Cola \n [2] Pepsi \n [3] Fanta \n [4] Sprite: ")
udito = input().strip()

match udito:
    case "1":
        print("A valasztott udito Coca Cola")
    
    case "2":
        print("A valasztott udito Pepsi")

    case "3":
        print("A valsztott udito Fanta")

    case "4":
        print("A valasztott udito Sprite")
