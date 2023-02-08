from os import system

num1: int = None
num2: int = None

print("kerem a szamot: ",end='')
num1=int(input())

print("kerem a masikat: ",end='')
num2=int(input())

for i in range(num2, num1, -1):
    print(i)