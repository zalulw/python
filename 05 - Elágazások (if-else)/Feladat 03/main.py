from os import system

num1: int = None

print("kérem a beolvasandó számot:", end='')
num1=int(input())

if (num1 >= -30 and num1 <= 40):
    print("A szám -30 és 40 között van")
else:
    print("A szám ninccs a tartományban")