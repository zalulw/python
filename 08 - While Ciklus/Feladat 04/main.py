from os import system

sum: int= 0
temp: str = 0
numberToAdd: int = 0
tries: int=0

while (sum < 100):
    print("szam", end="")
    temp = input().strip()
    if (temp.isnumeric()):
        numberToAdd = int(temp)
        sum = sum + numberToAdd
        tries += 1
        print(f"osszeg: {sum}")
    else:
        print("Nem számot adott meg!")