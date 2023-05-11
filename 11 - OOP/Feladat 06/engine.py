class Engine:
    def __init__(self):
        self.horsepower: int = None
        self.fuelType:str = None
        self.cylinders:int = None
        self.compressionRatio:float = None

    def __str__(self)->str:
        return f"{self.horsepower} {self.fuelType} {self.cylinders} {self.compressionRatio}" 