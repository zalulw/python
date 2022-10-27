from os import system

numEgy: int = None
numKet: int = None
numHar: int = None
eredmeny: int = None

print("kerem az elso szamot az osszeadashoz:")
numEgy=int(input())

print("kerem a masodik szamot az osszeadashoz:")
numKet=int(input())

print("kerem a szamot a kivonashoz:")
numHar=int(input())

eredmeny = (numEgy + numKet) - numHar
print(f"az eredmeny {eredmeny}")