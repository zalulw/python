from os import system
import math

num1: int = None
num2: int = None
muvelet: str = None
osszEredmeny: int = None
kivEredmeny: int = None
szorEredmeny: int = None
osztEredmeny: int = None



print("kerem az elso szamot: ")
num1=int(input())

print("kerem a masodik szamot: ")
num2=int(input())

<<<<<<< HEAD
print("mit szeretne tenni a ket szammal (osszeadas, kivonas, szorzas, osztas): ")
muvelet=input().strip().lower()
=======
muvelet=(input("mit szeretne tenni a ket szammal (osszeadas, kivonas, szorzas, osztas): ")).lower().strip()
>>>>>>> 50f309e65a82688b327a55eb5193354b5754c54a
match muvelet:
    case"osszeadas":
        osszEredmeny=num1 + num2
        print(osszEredmeny)
    
    case"kivonas":
        kivEredmeny=num1 - num2
        print(kivEredmeny)

    case"szorzas":
        szorEredmeny=num1 * num2
        print(szorEredmeny)

    case"osztas":
        osztEredmeny=num1 / num2
        print(osztEredmeny)