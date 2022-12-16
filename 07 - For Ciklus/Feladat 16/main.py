from os import system

kezdoErtek:int = None
vegErtek:int = None

print("kerem a kezdoerteket: ")
kezdoErtek=int(input())

print("kerem a vegerteket: ")
vegErtek=int(input())

osszegParos = 0
osszegParatlan = 0
sumParos = 0
sumParatlan = 0
atlag:float=None

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 2 == 0):
        sumParos += i
        osszegParos += i
    else:
        sumParatlan += i
        osszegParatlan += i

atlag = (sumParatlan + sumParatlan) / (osszegParatlan + osszegParos)

print(f"az szamok atlaga {atlag}")