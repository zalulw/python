from os import system
import math

t: int = None
k: int = None
a: int = None
rectangle: int = None

print("kerem a teglalap szelesseget cm-ben: ")
rectangleWidth=int(input())
print("kerem a teglalap hosszat cm-ben: ")
rectangleLength=int(input())

print("[t] - terulet \n [k] - kerulet \n [a] - atlo")
rectangle=input()

match rectangle:
    case "t":
        t=int(rectangleLength * rectangleWidth)
        print(f"a terulet {t}cm2")
    
    case "k":
        k=int(2 * (rectangleLength * rectangleWidth))
        print(f"a kerulet {k}cm3")

    case "a":
        a=int((rectangleLength * rectangleLength) + (rectangleWidth * rectangleWidth))
        print(f"az atlo {a}cm")