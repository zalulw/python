from os import system

kezdoertek: int = None
vegertek: int = None

print("kerem a kezdoerteket: ", end='')
kezdoertek=int(input())

print("kerem a vegerteket: ", end='')
vegertek=int(input())

sum=0

for i in range(kezdoertek, vegertek):
    sum = sum + i

print(sum)