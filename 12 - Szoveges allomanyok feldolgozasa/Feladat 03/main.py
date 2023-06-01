from volleyball import Player
from typing import *
from volleyballIO import *
from services import *

fileName:str = "data/adatok.txt"
players: List[Player] = importPlayers(fileName)

#össz adat kiirasa
writeToConsole(players)