class Manufacturer:
    def __init__(self):
        self.brand: str = None
    
    def __str__(self)->str:
        return f"{self.brand}"