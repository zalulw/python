from os import system

num: int = None

print("kérem a számot:", end='')
num=int(input())

if (num >= 0 and num <= 9):
    print("A szám egyjegyű")

elif(num >= 10 and num <= 90):
    print("a szám kétjegyű")

elif(num >=100 and num <= 999):
    print("a szám háromjegyű")
    

print("a szám négy vagy több jegyű")