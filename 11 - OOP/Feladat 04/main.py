from manufacturer import *
from model import *
from filtering import *
from speed import *

manufactuter: Manufacturer() = Manufacturer()
manufactuter.brand = "Phillips"

model: Model() = Model()
model.type = "SM8889"

filtering: Filtering() = Filtering()
filtering.type ="micro"

speed: Speed() = Speed()
speed.speed = 3