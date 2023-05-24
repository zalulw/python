import datetime

class Book:
    def __init__(self):
        super().__init__()
        self.writerFirstName: str = None
        self.writerSurname: str = None
        self.writerBirthday: datetime = datetime()
        self.bookTitle:str = None
        self.ISBN:str = None
        self.publisher:str = None
        self.publishYear:int = None
        self.price:float=None
        self.theme:str = None
        self.pageNumber:int = 0
        self.writerHonorarium: float = 0
    
    def __str__(self) -> str:
        return f"{self.writerFirstName} {self.writerSurname} - {self.bookTitle} {self.publishYear}"