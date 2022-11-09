from os import system

num1: int = None

print("kérem a beolvasandó számot:", end='')
num1=int(input())

if (num1 >= 0):
    print("A szám pozitív")
    
else:
    print("a szám negatív")
