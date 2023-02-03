from os import system

sum = 0
number: int = None
tries: int = 0

while(sum <= 100):
    print("ertek: ")
    number=int(input())

    sum += number
    tries += 1
    
    print(f"az ertek {sum}")
    print(f"{tries}. proba")
        