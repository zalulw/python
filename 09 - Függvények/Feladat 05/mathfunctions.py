from consoleIO import *

def calculateSameLetters() -> int:
    word1: str = getStringfromConsoleA()
    word2: str = getStringfromconsoleB()
    count = 0

    for letter in word1:
        if (letter in word2):
            count+=1

            word2 = word2.replace(letter, '', 1)

    return count