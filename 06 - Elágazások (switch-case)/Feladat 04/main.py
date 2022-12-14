from os import system
import math

num1: int = None
num2: int = None
muvelet: str = None




print("kerem az elso szamot: ")
num1=int(input())

print("kerem a masodik szamot: ")
num2=int(input())

print("mit szeretne tenni a ket szammal (osszeadas, kivonas, szorzas, osztas): ")
muvelet=input().strip().lower()
match muvelet:
    case"osszeadas":
        osszEredmeny=int(num1 + num2)
        print(osszEredmeny)
    
    case"kivonas":
        kivEredmeny=int(num1 - num2)
        print(kivEredmeny)

    case"szorzas":
        szorEredmeny=int(num1 * num2)
        print(szorEredmeny)

    case"osztas":
        osztEredmeny=int(num1 / num2)
        print(osztEredmeny)