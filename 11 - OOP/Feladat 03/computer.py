class CPU:
    def __init__(self):
        self.clockSpeed:float = None
        self.manufacturer:str = None
        self.model:str = None
        self.cacheSize:int = None
        self.cores:int = None



class GPU:
    def __init__(self):
        self.manufacturer:str = None
        self.clockSpeed: float = None
        self.model:str = None
        self.videoRAM:int = None

class RAM:
    def __init__(self):
        self.capacity:int = None
        self.manufacturer: str = None
        self.model:str = None
        self.speed:float = None
        self.latency: float = None

class storage:
    def __init__(self):
        self.capacity:float = None
        self.manufacturer: str = None
        self.model:str = None
        self.speed: float = None
        self.type: str = None

class motherboard:
    def __init__(self):
        self.manufacturer:str = None
        self.type:str = None

class computer:
    def __init__(self):CPU, GPU, RAM, storage, motherboard
    def __str__(self)->str:
        return f"{CPU} {GPU} {RAM} {storage} {motherboard}"

