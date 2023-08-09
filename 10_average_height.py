"""Calculates the average height of a list of students"""

student_heights = input("Input a list of student heights in cm: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_students = 0
for student in student_heights:
    number_of_students += 1

total_heights = 0
for height in student_heights:
    total_heights += height

average_heights = round(total_heights / number_of_students)
print(f"{average_heights}cm")
