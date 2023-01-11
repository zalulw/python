from os import system

kezdoErtek: int = None
vegErtek: int = None
osszeg = 0

print("kerem a kezdoerteket: ")
kezdoErtek=int(input())

print("kerem a vegerteket: ")
vegErtek=int(input())

for i in range(kezdoErtek, vegErtek, 2): #kettesevel lepked ( paratlan szamok)
    osszeg += i 
for i in range(kezdoErtek+1, vegErtek, 2): #kettesevel lepked (paros szamok)
    osszeg += (i*-1) #osszeg -= i 
print(osszeg)