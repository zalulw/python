from os import system
from random import randint

even: int=None
odd: int=None
tempEven: str = None
tempOdd: str = None
randomNum: int = None
average: int = None
devide: int = 0

while (even == None or even % 2 !=0):
    print("paros szam:", end="")
    tempEven = input().isnumeric()
    even = int(tempEven)

while (odd == None or odd % 2 != 1 or even >= odd):

    print("paros szamnal nagyobb paratlan szam:", end="")
    tempOdd = input().isnumeric()
    odd = int(tempOdd)


randomNum = randint(even, odd)
print(f"a random {randomNum}.")

if(abs(odd - randomNum) > abs(even-randomNum)):
    print(f"A {odd} messzebb van a randomszámtól({randomNum})")
else: 
    print(f"A {odd} messzebb van a randomszámtól({randomNum})")


average = (even + odd)/2

print(f"A két bekért szám átlaga: {average}")


for i in range(even, odd, 1):
    if (i % 4 == 0):
        devide += 1

print(f"A 4-el osztható számok száma: {devide}")