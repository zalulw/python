from os import system

kezdoErtek: int = None
vegErtek:int = None
darab = 0

print("kerem a kezdoerteket: ", end='')
kezdoErtek=int(input())

print("kerem a vegerteket: ", end='')
vegErtek=int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 3 == 0):
        darab += 1
print(darab)
