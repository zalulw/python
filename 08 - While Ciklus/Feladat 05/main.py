from os import system

sum = 0
number: int = None
limit: int = None
tries = 0

#+1 while cikl bekeri a hatarerteket
while(limit == None and limit > 100):
    print("hatarertek: ")
    limit=int(input())

#szambekeres
while(limit >= 100 or sum < limit):
    print("ertek: ")
    number=int(input())

    sum += number
    tries += 1

    if(sum >= limit):
        print(f"elerte az hatarerteket ({limit})")
        print(f"{tries} probaba telt")