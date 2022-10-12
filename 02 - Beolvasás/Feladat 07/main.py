from os import system
from platform import release
system("cls")

brand: str = None
modell: str = None
carType: str = None
kobcenti: int = None
releaseDate: int = None

print("Kérem az autó márkáját:", end='')
brand=str(input())

print("Kérem az autó modellét:", end='')
modell=str(input())

print("Kérem az autó típusát", end='')
carType=str(input())

print("Hány köbcentis:", end='')
kobcenti=int(input())

print("Kérem a megjelenési évét:", end='')
releaseDate=int(input())

print(f"Márka: {brand} \n Modell: {modell} \n Típus: {carType} \n Köbcenti: {kobcenti} \n Megjelenés: {releaseDate}")