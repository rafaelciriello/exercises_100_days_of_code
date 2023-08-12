"""Calculating the average of the grades of the class"""

student_score = input("Input a list of student score: ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")
