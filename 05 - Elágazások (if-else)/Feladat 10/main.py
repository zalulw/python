from os import system

num: int = None

print("kérem a számot:", end='')
num=int(input())
if (num % 3 == 0 and num % 2 == 0):
    print("ZIZI")

    
elif (num % 3 == 0):
    print("BAZ")

elif (num % 2 == 0):
    print("BIZ")

else:
    print("a szám nem osztható se kettővel se hárommal.")
