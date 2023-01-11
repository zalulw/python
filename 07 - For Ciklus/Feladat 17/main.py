from os import system

kezdoErtek: int = None
vegErtek:int = None
atlag: float = None
sum = 0
osszeg = 0
darab = 0

print("kerem a kezdoerteket: ")
kezdoErtek=int(input())

print("kerem a vegerteket: ")
vegErtek=int(input())

for i in range (kezdoErtek, vegErtek, 1):
    sum += i
    osszeg += 1

atlag = sum/osszeg


print(atlag)