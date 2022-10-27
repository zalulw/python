from os import system

num: int = None

print("kerem a szamot:", end='')
num=int(input())

if (num % 2 == 0 and num > 0 and num % 5 == 0):
    print("A szám páros, osztható öttel és pozitív")
elif (num % 2 != 0 and num > 0 and num % 5 == 0):
    print("A szám páratlan, osztható öttel és pozitív")
elif (num % 2 != 0 and num < 0 and num % 5 == 0):
    print("a szám páratlan, osztható öttel és negatív")
elif (num % 2 == 0 and num < 0 and num % 5 == 0):
    print("a szám páros, osztható öttel és negatív")
elif (num % 2 == 0 and num < 0 and num % 5 != 0):
    print("a szám páros, nem osztható öttel és negatív")
elif (num % 2 != 0 and num > 0 and num % 5 != 0):
    print("a szám páratlan, nem osztható öttel és pozitív")
elif (num % 2 != 0 and num < 0 and num % 5 != 0):
    print("a szám páratlan, pozitív és nem osztható öttel")
else:
    print("a szám 0")