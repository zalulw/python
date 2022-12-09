from os import system

kezdoertek: int = None
vegertek: int = None

print("kerem a kezdoerteket: ", end='')
kezdoertek=int(input())

print("kerem a vegerteket:", end='')
vegertek=int(input())

if vegertek % 2 == 0:
    for i in range(vegertek, kezdoertek, 2):
        print(i)

else:
    for i in range(vegertek+1, kezdoertek, 2):
        print(i)
