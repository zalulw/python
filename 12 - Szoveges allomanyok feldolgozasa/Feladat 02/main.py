from book import Book
from typing import *
from bookIO import readBooksFromFile, writeBooksToFile
from services import *

fileName:str = "data/adatok.txt"
books: List[Book] = readBooksFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeToConsole(books)

#Keressük ki az informatika témajú könyveket 
#mentsük el őket az informatika.txt állömányba
filteredBooks: List[Book] = getBooksByTheme("informatika", books)
writeBooksToFile("informatika.txt", filteredBooks)

#Az 1900.txt állományba mentsük el azokat a könyveket
#amelyek az 1900-as években íródtak
booksFromPublishInterval: List[Book] = getBooksByPublishYearInterval(1900, 1999, books)
writeBooksToFile("1900.txt", booksFromPublishInterval)

#Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe
#és a sorbarakott.txt állományba mentsük el.
sortBooksByPageNumberDescending(books)
writeBooksToFile("sorbarakott.txt", books)