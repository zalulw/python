from os import system

num = 0
osszeg = 0
db = 0

while ((num < 1) or (num > 99)):
    print("ketjegyu paros szam kell", end='')
    num=int(input())

for i in range(0, num, 1):
    if (i % 2 == 0):
       print("paros szamok ", end='')
    print(i)
