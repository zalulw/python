from os import system

number: int = None
temp: str = None
devideableByFive: int = None
devideableByEleven: int = None

while (number == None and (number > 0) and (number < 99)): 
    print("ketjegyu szam:", end="")
    temp = input()
    if (temp.isnumeric() and len(temp) < 3 and len(temp) > 1):
        number = int(temp)

print(f"0 és a szám közötti páros számok:", end="")

for i in range (0, number, 1):
    if (i % 2 == 0):
        print(f"{i}, ", end="")
    if (i % 5 == 0):
        devideableByFive += i
    if (i % 11 == 0):
        devideableByEleven += 1

print("Számok amelyeket, ha elosztasz 7-el 3-mat kapsz maradékul:", end="")
for i in range (0, number + 1, 1):
    if (i % 7 == 3):
        print(f"{i}, ", end="")

print(f"\n 5-el osztható számok összege: {devideableByFive}")
print(f"\n 11-el osztható számok száma: {devideableByEleven}")