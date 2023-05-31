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

#informatika temaju konyvek megkeresese, fileba irasa
filteredBooks: List[Book] = getBooksByTheme("informatika", books)
writeBooksToFile("informatika.txt", filteredBooks)

#Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
booksFromPublishInterval: List[Book] = getBooksByPubYear(1900, 1999, books)
writeBooksToFile("1900.txt", booksFromPublishInterval)