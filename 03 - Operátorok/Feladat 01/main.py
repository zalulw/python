from os import system

numEgy: int = None
numKet: int = None
eredmeny: int = None

print("Kérem az egyik számot:")
numEgy=int(input())

print("Kérem a másik számot:")
numKet=int(input())

eredmeny = numEgy + numKet

print(f"Az eredmeny {eredmeny}")