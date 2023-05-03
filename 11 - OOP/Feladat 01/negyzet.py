#osztály
class Negyzet:
    #konstruktor
    def __init__(self, a: float = 0):
        super().__init__()
        #adattag
        self.oldal: float = a
    #függvény(ek)
    def terulet(self) -> float:
        return self.oldal * self.oldal

    def kerulet(self) -> float:
        return 4 * self.oldal 