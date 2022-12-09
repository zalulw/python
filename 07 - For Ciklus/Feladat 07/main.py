from os import system

a: int = None
b: int = None

print("kerem a kezdoerteket")
a=int(input())
 
print("kerem a vegerteket")
b=int(input())

for i in range(b, a, -1):
    print(i)