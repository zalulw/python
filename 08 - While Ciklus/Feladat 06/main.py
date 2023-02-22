from os import system

age: int = None


while(age == None or age == int):
    print("kor: ")
    age=int(input().isnumeric())

if (age > 0 and age <= 6):
    print("gyermek")

elif (age >= 7 and age <= 18):
    print("iskolás")

elif (age >= 19 and age <= 65):
    print("dolgozo")

elif (age > 65):
    print("nyugdijas")

else:
    print("nem szam")