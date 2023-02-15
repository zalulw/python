from os import system

sum: float = None
temp: str=None
month: int=0

while (sum == None):
    print("penz: ", end="")
    temp = input()
    if (temp.isnumeric()):
        sum = float(temp)

while (sum < 100000):
    sum *= 1.02
    month += 1
    print(f"A száz ezer forintot {month} honap alatt fogja elérni a megtakarítás!")
