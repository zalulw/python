from book import Book
from typing import *
from os import *
import os

def readBooksFromFile(fileName: str) -> List[Book]:
    books: List[Book] = []
    
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() #Antalfai Martin	3,53
                data = oneLine.split('\t')
    return books