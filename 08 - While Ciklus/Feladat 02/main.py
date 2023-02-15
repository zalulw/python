from os import system

name: str = None
temp: str = None

while(name == None or len(name) < 2 ):
    print("Kérem írja be a nevét: ", end="")
    name = input().strip()

print(f"Üdvözlöm {name}!")