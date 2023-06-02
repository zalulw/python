from volleyball import Player
from typing import *

def writeToConsole(players: List[Player]) -> None:
    for player in players:
        print(player)

def getPlayersByPosition(position: str, players: List[Player]) -> List[Player]:
    filteredPlayers: List[Player] = []

    for player in players:
        if(player.position == position):
            filteredPlayers.append(player)
    
    return filteredPlayers

def getPlayersByTeam(team: str, players: List[Player]) -> List[Player]:
    filteredPlayers: List[Player] = []
    for player in players:
        if(player.team == team):
            filteredPlayers.append(player)
    
    return filteredPlayers