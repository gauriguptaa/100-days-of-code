# Using Dictionary comprehension to randomly assign scores to the students
import random

if __name__ == '__main__':
    students = ['Ira', 'Vishal', 'Beth', 'Susana', 'Gauri', 'Jennifer', 'Brad', 'Angelina', 'Irina', 'Gigi', 'Bella']
    students_report = {student: random.randint(1, 100) for student in students}
    print(students_report)

    # OUTPUT {'Ira': 60, 'Vishal': 56, 'Beth': 54, 'Susana': 56, 'Gauri': 36}
    # Print the names of students who have passed.

    passed_students = {student for student in students_report if students_report[student] >= 60}
    passed_students_dict = {key: value for(key, value) in students_report.items() if value >= 60}
    print(passed_students)
    print(passed_students_dict)
# {'Ira': 100, 'Vishal': 79, 'Beth': 17, 'Susana': 87, 'Gauri': 70, 'Jennifer': 58, 'Brad': 31, 'Angelina': 76,
# 'Irina': 81, 'Gigi': 23, 'Bella': 18} {'Vishal', 'Ira', 'Irina', 'Susana', 'Angelina', 'Gauri'}
