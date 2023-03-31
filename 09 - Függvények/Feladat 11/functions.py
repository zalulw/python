hourWage: int = 1000
overtime: int = 1500

def calculateWage(hours: int):
    salary: int = None
    if (hours < 40):
        salary = hours * hourWage
    else:
        salary = 40 * hourWage + (hours - 40) * overtime
         
    return salary