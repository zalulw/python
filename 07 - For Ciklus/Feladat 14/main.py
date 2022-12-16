from os import system

kezdoErtek: int = None
vegErtek: int = None

print("kerem a kezdoerteket: ")
kezdoErtek=int(input())

print("kerem a vegerteket: ")
vegErtek=int(input())

sum1 = 0
sum2 = 0

for i in range(kezdoErtek, vegErtek):
    if (i % 7 == 0):
        sum1 = sum1 + i
    elif (i % 5 == 0):
        sum2 = sum2 + i



if (sum1 > sum2):
    print("a hettel oszthato szamok osszege nagyobb")
else:
    print("az ottel oszthato szamok osszege nagyobb")
