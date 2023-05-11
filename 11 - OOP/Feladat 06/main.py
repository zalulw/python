from body import Body
from brakes import Brakes
from electrics import Electrics
from engine import Engine
from suspension import Suspension
from tires import Tires
from transmission import Transmission

body: Body() = Body()
body.length = 465.582

brakes: Brakes() = Brakes()
brakes.type = "Disc"

electrics: Electrics() = Electrics()
electrics.batteryVoltage = 12.6

engine: Engine() = Engine()
engine.fuelType = "Gasoline"

suspension: Suspension() = Suspension()
suspension.type = "Dual axis strut"

tires: Tires() = Tires()
tires.diameter = "215/55"

transmission: Transmission() = Transmission()
transmission.gearRatio = "2.818:1."