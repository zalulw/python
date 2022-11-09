from os import system

num1: int = None
num2: int = None


print("kerem az elso szamot_", end='')
num1=int(input())

print("kerem a masodik szamot:", end='')
num2=int(input())

if (num1 < num2):
    print(f"{num1} {num2}")
elif (num1 == num2):
    print(f"{num1} es {num2} egyenlo")
else:
    print(f"{num2} {num1}")