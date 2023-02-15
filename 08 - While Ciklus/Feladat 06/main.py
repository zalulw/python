from os import system

age: int = None

#szamellenorzos
while(age == None or (age < 100) or (age > 0)):
    print("kor: ")
    age=int(input())

if (age > 0 and age <= 6):
    print("gyermek")

elif (age >= 7 and age <= 18):
    print("iskolás")

elif (age >= 19 and age <= 65):
    print("dolgozo")

else:
    print("nyugdijas")