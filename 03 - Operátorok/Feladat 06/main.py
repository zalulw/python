from os import system

numEgy: float = None
numKet: float = None
numHar: float = None
eredmeny: float = None

print("kerem az elso szamot")
numEgy=float(input())

print("kerem a masodik szamot")
numKet=float(input())

print("kerem a harmadik szamot:")
numHar=float(input())

numEgy = numEgy + 0.5
numKet = numKet - 0.7

eredmeny = (numEgy * numKet) % numHar
print(f"a maradek {eredmeny}")