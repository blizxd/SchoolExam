from typing import List, Dict


class gradeInfo:

    grades = {}

    def __init__(self, grade):
        self.numberOfStudents: int = 0
        self.totalDistance: float = 0
        self.grade = grade

    def addData(self, distance):
        self.totalDistance += round(distance, 2)

    def __str__(self) -> str:
        return f"{self.grade} {self.numberOfStudents} {self.totalDistance}"

    @staticmethod
    def addGradeOrUpdate(grade, distance):
        if grade in gradeInfo.grades.keys():
            gradeInfo.grades[grade].addData(distance)
            gradeInfo.grades[grade].numberOfStudents += 1
        else:
            gradeInfo.grades[grade] = gradeInfo(grade)
            gradeInfo.grades[grade].numberOfStudents = 1
            gradeInfo.grades[grade].addData(distance)

    @staticmethod
    def printDataToFile(file):
        for k, v in gradeInfo.grades.items():
            file.write(str(v) + "\n")


with open("./U1.txt", "r") as file:
    for line in file.readlines()[1::]:  # Skip 1st line

        line = [int(x) for x in line.split()]

        if (0 in line):
            continue

        grade = line[0]
        feetLength = line[1]
        totalDistance = feetLength*sum(line[2::])/100_000
        gradeInfo.addGradeOrUpdate(grade, totalDistance)

with open("./U1rez.txt", "w") as file:
    gradeInfo.printDataToFile(file)
