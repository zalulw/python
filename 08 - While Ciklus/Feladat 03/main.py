from os import system
import random

randomNum = random.randint(0, 9)
num: int = None
tries: int = 0

print("0 es 9 kozti szamot talalja ki 5 probabol!", end='')

while(tries < 5 or num != randomNum):
    print("rookie mistake baby bozo 🤡🤡🤡", end='')
    num=int(input())
    tries += 1
    if(tries == 5):
        print("vege a mokanak kis krapek ocsipok ocskos")
        break

    if(num == randomNum):
        print("gratulalok 🎉🎉🎉🎉🎉🎉")
