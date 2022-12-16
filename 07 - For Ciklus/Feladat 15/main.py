from os import system

kezdoErtek:int=None
vegErtek:int=None
osszeg=0

print("kerem a kezdoerteket")
kezdoErtek=int(input())

print("kerem a vegerteket")
vegErtek=int(input())

for i in range(kezdoErtek, vegErtek):
    if (i % 2 != 0):
        if (i % 3 == 0):
            osszeg=osszeg + 1
print(osszeg)
