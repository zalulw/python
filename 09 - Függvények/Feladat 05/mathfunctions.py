def calculateSameLetters(text1: str, text2: str) -> int:
    intersection = 0

    for i in text1:
        if (i in text2 and i not in intersection):
            intersection += 1
            text2 = text2.replace(i, '', 1)

    return intersection
# def calculateSameLetters(text1: str, text2: str) -> int:
#     text1 = str
#     text2 = str
#     intersection = 0


#     for i in text1:
#         if (i in text2.find(i) > 0 and intersection.find(i) == 0):
#             intersection+=1

#             text2 = text2.replace(i, '', 1)

#     return intersection