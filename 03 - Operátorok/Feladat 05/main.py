from os import system 

numEgy: int = None
numKet: int = None
numHar: int = None
numNegy: int = None
eredmeny: float = None

print("kerem az osszeadashoz az elso szamot")
numEgy=int(input())

print("kerem az osszeadashoz a masodik szamot")
numKet=int(input())

print("kerem a kivonashoz az elso szamot")
numHar=int(input())

print("kerem a kivonashoz a masodik szamot")
numNegy=int(input())

eredmeny=(numEgy + numKet) / (numHar - numNegy)
print(f"az eredmeny {eredmeny}")