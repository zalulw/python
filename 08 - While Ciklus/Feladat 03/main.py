from os import system
import random

randomNum = random.randint(0, 9)
num: int = None
tries: int = 0

print("0 es 9 kozti szamot talalja ki 5 probabol!", end='')

while(tries < 5 and num != randomNum):
    print("hibas", end='')
    num=int(input())
    tries += 1
    if(tries == 5):
        print("nincs tobb proba")
        break

if(num == randomNum):
    print("gratulalok 🎉🎉🎉🎉🎉🎉")
