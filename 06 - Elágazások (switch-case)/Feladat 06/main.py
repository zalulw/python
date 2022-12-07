from os import system
import math

t: int = None
k: int = None
a: float = None
rectangle: int = None

print("kerem a teglalap szelesseget cm-ben: ")
rectangleWidth=int(input())
print("kerem a teglalap hosszat cm-ben: ")
rectangleLength=int(input())

print("[t] - terulet \n [k] - kerulet \n [a] - atlo")
rectangle=input().lower().strip()

match rectangle:
    case "t":
        t=rectangleLength * rectangleWidth
        print(f"a terulet {t}cm2")
    
    case "k":
        k=2 * (rectangleLength + rectangleWidth)
        print(f"a kerulet {k}cm3")

    case "a":

        a=math.sqrt(pow(rectangleLength, 2) + pow(rectangleWidth, 2))
        print(f"az atlo {a}cm")