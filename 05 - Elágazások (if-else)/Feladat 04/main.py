from os import system

num1: int = None
num2: int = None

print("kérem az első számot:", end='')
num1=int(input())

print("kérem a második számot:", end='')
num2=int(input())

if (num1 > num2):
    print(f"a nagyobb szám a(z) {num1}")

elif (num1 == num2):
    print(f"a két szám egyenlő")

else:
    print(f"A(z) {num2} a nagyobb szám")
