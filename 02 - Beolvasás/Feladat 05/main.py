from os import system

favoriteBand: str = None
bestSong: str = None
songLegth: int = None

print("Kérem a kedvenc együttesét")
favoriteBand=str(input())

print("Kérem a legjobb számukat")
bestSong=str(input())

print("kérem a szám hosszát percben")
songLegth=int(input())

print(f"Az ön kedvenc együttesének, {favoriteBand} a legjobb száma {bestSong} melynek hossza {songLegth} perc")