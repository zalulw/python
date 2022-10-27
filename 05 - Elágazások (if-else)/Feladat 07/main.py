from os import system

num: int = None

print("kérem az osztót")
num=int(input())

if (num % 5 == 0):
    print("a szám osztható öttel")
else:
    print("a szám nem osztható öttel")