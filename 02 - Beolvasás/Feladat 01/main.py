from os import system

name: str = None

print(f"Kerem adja meg a nevet: ", end="")
name = str(input())

system('cls')

print(f"Udvozlom, {name}")