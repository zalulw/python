from os import system

a: int = None
b: int = None

print("kerem a kezdoerteket: ", end='')
a=int(input())

print("kerem a vegerteket: ", end='')
b=int(input())

if (a % 2 == 0):
    for i in range(a+1, b, 2):
        print(i)

else:
    for i in range(a, b, 2):
        print(i)