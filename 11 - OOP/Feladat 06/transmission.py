class Transmission:
    def __init__(self):
        self.gears:int = None
        self.type:str = None
        self.gearRatio: str = None

    def __str__(self)->str:
        return f"{self.gearRatio} {self.gears} {self.type}" 