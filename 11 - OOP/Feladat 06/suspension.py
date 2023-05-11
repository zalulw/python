class Suspension:
    def __init__(self):
        self.type:str = None
        self.shockAbsorberType: str = None
        self.springType:str = None
        self.suspensionTravel: int = None

    def __str__(self)->str:
        return f"{self.type} {self.shockAbsorberType} {self.springType} {self.suspensionTravel}" 