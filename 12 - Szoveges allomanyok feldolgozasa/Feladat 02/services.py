from book import *
from typing import *

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)

def getBooksByTheme(theme:str, books:List[Book])->List[Book]:
    filteredBooks: List[Book] = []

    for book in books:
        if(book.theme == theme):
            filteredBooks.append(book)

    return filteredBooks

def getBooksByPubYear(start:int, end:int, books:List[Book])->List[Book]:
    filteredBooks: List[Book] = []

    for book in books:
        if(book.publishYear >= start and book.publishYear <= end):
            filteredBooks.append(book)

    return filteredBooks