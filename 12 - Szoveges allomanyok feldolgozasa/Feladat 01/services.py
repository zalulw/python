from typing import *
from student import Student

def calculateAverage(students: List[Student]) -> float:
    sum: float = 0

    for student in students:
        sum += student.average 

    return sum/len(students)

def getBestStudent(students: List[Student]) -> float:
    bestStudent: Student = students[0] #referencia érték

    for index in range(1, len(students), 1):
        if(students[index].average > bestStudent.average):
            bestStudent = students[index]
    
    return bestStudent
