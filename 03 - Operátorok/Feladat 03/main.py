from os import system

numEgy: int = None
numKet: int = None
numHar: int = None
eredmeny: int = None

print("kerem az elso szamot a kivonashoz:")
numEgy=int(input())

print("kerem a masodik szamot a kivonashoz:")
numKet=int(input())

print("kerem a szorzot:")
numHar=int(input())

eredmeny = (numEgy - numKet) * numHar
print(f"az eredmeny {eredmeny}")