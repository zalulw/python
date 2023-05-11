class Brakes:
    def __init__(self):
        self.type:str = None
        self.material:str = None
        self.caliper:str = None
        self.rotorSize:float = None

    def __str__(self)->str:
        return f"{self.type} {self.material} {self.caliper} {self.rotorSize}" 