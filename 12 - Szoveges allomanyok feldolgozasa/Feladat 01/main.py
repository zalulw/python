from typing import *
from student import Student
from studentIO import importStudents
from services import *

students: List[Student] = importStudents()
#kiiratjuk a diakok adatait
print("Az osztaly tanuloi")
for student in students:
    print(student)

#megszamoljuk a tanulok szamat
countOfClass: int = len(students)
print(f"\n\naz osztalynak {countOfClass} tanuloja van \n\n")

classAverage: float = calculateAverage(students)
print(f"az osztaly atlaga: {classAverage:1.2f}")

bestStudent: Student = getBestStudent(students)
print(f"\n\nA legjobb tanulo {bestStudent}\n\n")