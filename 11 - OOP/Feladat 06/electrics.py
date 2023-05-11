class Electrics:
    def __init__(self):
        self.batteryCapacity:float = None
        self.batteryVoltage:float = None
        self.powerConsumption:float = None

    def __str__(self)->str:
        return f"{self.batteryCapacity} {self.batteryVoltage} {self.powerConsumption}" 