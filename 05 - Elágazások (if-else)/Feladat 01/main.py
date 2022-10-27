from os import system

num1: int = None

print("kérem a beolvasandó számot:", end='')
num1=int(input())

if (num1 >= 0):
    print("a szám nagyobb nullánál")
else:
    print("a szám kisebb nullánál")
