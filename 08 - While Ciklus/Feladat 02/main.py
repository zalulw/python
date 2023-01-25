from os import system
system('cls')

name: str = None
nameLength: int = None

print("adja meg a nevét: ",end='')
name=str(input())
len(name)

while(name == str):
    if (len(name) < 2):
        print("a nev nem eleg hosszu")
    else:
        print(f"Üdvözöljük {name}")
