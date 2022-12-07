from os import system
import math

r1: int = None
r2: int = None
parhuzamos: float = None
soros: int = None

print("kerem az elso ellenallas eredo erteket: ")
r1=int(input())

print("kerem a masodik ellenallas eredo erteket: ")
r2=int(input())


print("milyen fajta ellenallas [p] parhuzamos vagy [s] soros: ")
kotes=input().strip().lower()

match kotes: 
    case "p | P":
        parhuzamos=(r1*r2)/(r1+r2)
        print(f"az ellenallas erteke {parhuzamos}")

    case "s | S":
        soros=r1+r2
        print(f"az ellenallas erteke {soros}")