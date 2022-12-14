from os import system

kezdoErtek: int = None
vegErtek:int = None

print("kerem a kezdoerteket: ", end='')
kezdoErtek=int(input())

print("kerem a vegerteket: ", end='')
vegErtek=int(input())

paros=0
paratlan=0

for i in range(kezdoErtek, vegErtek):
    if (i % 2 == 0):
        paros=paratlan + i
    else:
        paratlan = i

print(paros, paratlan)

if (paros > paratlan):
    print("a paros szamokbol tobb van")

else:
    print("a paratlan szamokbol tobb van")