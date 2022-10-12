from os import system

name: str = None
birthDate: int = None

print("neve: ")
name = str(input())

print("szuletesi eve: ")
birthDate = int(input())

system('cls')

print(F"{name} {birthDate}-ben szuletett")
