from os import system

num: int = None

print("kérem a számot", end='')
num=int(input())

if (num >= 10 and num <= 20):
    print("a szám 10 és 20 között van", end='')

elif (num <= -10 and num >= -20):
    print("a szám -10 és 20 között van")
    
else: 
    print("a szám nincs benne a tartományban")