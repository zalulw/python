def game(real: int) -> int:
    guess: str = None
    while (guess != real):
        print(f"tipp: ", end="")
        guess = input().strip()

        if (not guess.isnumeric()):
            print("Nem számot adott meg!")
            continue
        
        guess = int(guess)
        if (guess < real):
            print("nagyobb")
        elif (guess > real):
            print("kisebb")
        else:
            print("helyes!")