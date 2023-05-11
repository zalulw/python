class Tires:
    def __init__(self):
        self.diameter: str = None
        self.type: str = None
        self.speedRating: float = None
        self.load:float = None

    def __str__(self)->str:
        return f"{self.diameter} {self.type} {self.speedRating} {self.load}" 