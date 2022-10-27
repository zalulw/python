from os import system
from platform import release

name: str = None;
vehicleType: str = None
modell: str = None
releaseYear: int = None
cost: float = None


print("Neve:", end='')
name=str(input())

print(f"Jó napot kedves {name}. Miben segíthetek?")

print("Engem érdekelne egy: ",end='')
vehicleType=str(input())

print(f"Értem, egy {vehicleType}. Melyik modell?")
modell=str(input())

print("Évjárat?")
releaseYear=int(input())

print("Hány milliót szánna rá?")
cost=float(input())


print(f"Sajnálom kedves {name}, de jelenleg {releaseYear}-es évjáratú és {vehicleType} {modell} nincs a kínálatunkban ami beleférne a(z) {cost} millió forintba")