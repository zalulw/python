from os import system

number: int = None
temp: str = None

while (number == None or number < 100 or number > 999):
    print("Adjon meg egy 3 jegyű számot:")
    temp = input()
    if (temp.isnumeric()):
        number = int(temp)

if (number % 7 == 0):
    print("A szám osztható 7-el.")
else:
    print("A szám nem osztható 7-el.")