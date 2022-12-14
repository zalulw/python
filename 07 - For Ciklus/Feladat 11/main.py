from os import system

kezdoErtek: int = None
vegErtek:int = None

print("kerem a kezdoerteket: ", end='')
kezdoErtek=int(input())

print("kerem a vegerteket: ", end='')
vegErtek=int(input())

sum = 0
szorzat: int = 1

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 2 == 0):
        sum = sum + 1
    else:
        szorzat = szorzat * 1

print(sum, szorzat)