from os import system

numEgy: int = None
numKet: int = None
numHar: int = None
eredmeny: float = None

print("kerem a szorzandot:")
numEgy=int(input())

print("kerem a szorzot:")
numKet=int(input())

print("kerem az osztot:")
numHar=int(input())

eredmeny=(numEgy * numKet) / numHar
print(f"az eredmeny {eredmeny}")