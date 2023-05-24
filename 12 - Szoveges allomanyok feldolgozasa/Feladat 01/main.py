from typing import *
from student import Student
from studentIO import *
from services import *

students: List[Student] = importStudents()
#kiiratjuk a diakok adatait
print("Az osztaly tanuloi")
for student in students:
    print(student)

#megszamoljuk a tanulok szamat
countOfClass: int = len(students)
print(f"\n\naz osztalynak {countOfClass} tanuloja van \n\n")
#osztalyatlag
classAverage: float = calculateAverage(students)
print(f"az osztaly atlaga: {classAverage:1.2f}")
 #legjobb tanulo
bestStudent: Student = getBestStudent(students)
print(f"\n\nA legjobb tanulo {bestStudent}\n\n")
#tanulok az atlag felett .txt fileba
aboveAverage:List[student]=studentsAboveAverage(students, classAverage)
writeStudentsInFile(aboveAverage, "atlagfelett.txt")
#van e kituno tanulo
exists:bool = isAnyExcellentStudent(students)
if(exists):
     print("Van kituno tanulo")
else: 
    print("nincs kituno tanulo")