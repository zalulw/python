import os
from typing import *
from io import open
from volleyball import Player


def importPlayers(fileName: str) -> List[Player]:

    players: List[Player] = []    
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split('\t')

                player = Player()
                player.name = data[0]
                player.height = int(data[1])
                player.position = data[2]
                player.nationality = data[3]
                player.team = data[4]
                player.homeCountry = data[5]

                players.append(player)
    
            return players
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return []
        
