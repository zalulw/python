from consoleIO import *
from convert import *


amount: float = getAmountfromConsole()
currency: str = getCurrencyfromConsole()

convertedAmount: float = convert(currency, amount)

print(convertedAmount, currency)

