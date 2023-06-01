class Player:
    def __init__ (self) -> None:
        super().__init__()
        self.name: str = None
        self.height: int = 0
        self.position: str = None
        self.nationality: str = None
        self.team: str = None
        self.homeCountry: str = None

    def __str__(self) -> str:
        return f"{self.name}, {self.height}, {self.position}, {self.nationality}, {self.team}, {self.homeCountry}"