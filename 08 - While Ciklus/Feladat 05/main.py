from os import system

sum = 0
number: int = None
limit: int = None
tries = 0

print("hatarertek: ")
limit=int(input())

while(limit >= 100 and sum < limit):
    print("ertek: ")
    number=int(input())

    sum += number
    tries += 1

    if(sum >= limit):
        print(f"elerte az hatarerteket ({limit})")
        print(f"{tries} probaba telt")