from bookIO import *
from book import *
from services import *
from datetime import date 
from typing import *
from os import system
from services import *

fileName:str = "data/adatok.txt"
books: List[Book] = readBooksFromFile(fileName)

#írja ki az össz adatot
writeToConsole(books)