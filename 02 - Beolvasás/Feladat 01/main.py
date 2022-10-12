from os import system

name: str = None

print("Adja meg a nevét")
name = str(input("Kérem a nevét: "))

system("cls")

print(f"Udvozlom {name}")