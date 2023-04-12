def game(real: int) -> int:
    guess: str = None
    count: int = 0
    while (guess != real):
        print(f"tipp: ", end="")
        guess = input().strip()

        if (not guess.isnumeric()):
            print("Nem számot adott meg!")
            continue
        
        guess = int(guess)
        if (guess < real):
            count += 1
            print("nagyobb")
        elif (guess > real):
            count += 1
            print("kisebb")
        else:
            print("helyes!")

    return count