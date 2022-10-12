from os import system
from platform import release
system("cls")

favoriteMovie: str = None
releaseDate: int = None
director: str = None
mainActor: str = None

print("Kérem a kedvenc filme címét:",end='')
favoriteMovie=str(input())

print("Kérem a megjelenés évét:",end='')
releaseDate=int(input())

print("Kérem a rendező nevét:",end='')
director=str(input())

print("Kérem a főszereplő nevét:",end='')
mainActor=str(input())

print(f"{releaseDate}-ban/ben {director} rendezésében megjelent a/az {favoriteMovie} című film {mainActor} főszereplésével!")