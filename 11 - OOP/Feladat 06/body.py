class Body:
    def __init__(self):
        self.length:float = None
        self.width:float = None
        self.height:float = None
        self.weight:float = None

    def __str__(self)->str:
        return f"{self.length} {self.width} {self.height} {self.height} {self.weight}" 