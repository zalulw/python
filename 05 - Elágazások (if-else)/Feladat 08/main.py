from os import system

num: int = None

print("kérem az osztót")
num=int(input())

if (num % 6 == 0 and num % 4 == 0):
    print("a szám osztható néggyel és hattal is")
else:
    print("a szám nem osztható vagy néggyel vagy hattal")