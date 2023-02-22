from os import system

sum = 0
number: int = None
limit: int = 0
tries = 0


while(limit < 100):
    print("hatarertek: ")
    temp = input().strip()
if (temp.isnumeric()):
    limit==temp

while(sum < limit):
    print("ertek: ")
    number=int(input().isnumeric())

    sum += number
    tries += 1

print(f"elerte az hatarerteket ({limit})")
print(f"{tries} probaba telt")