from book import Book
import os
from typing import *
from io import open
from datetime import datetime

def readBooksFromFile(fileName: str) -> List[Book]:
    books: List[Book] = []
    book: Book = None
    
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split('\t')
        
                book= Book()
                book.writerFirstName=data[0]
                book.writerSurname=data[1]
                book.writerBirthday = datetime.fromisoformat(data[2])
                book.bookTitle = data[3]
                book.ISBN = data[4]
                book.publisher = data[5]
                book.publishYear = int(data[6])
                book.price = float(data[7])
                book.theme = data[8]
                book.pageNumber = int(data[9])
                book.writerHonorarium = float(data[10])

                books.append(book)


        return books

    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []