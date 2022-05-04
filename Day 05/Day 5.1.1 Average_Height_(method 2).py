student_heights = input("Input a list of student heights  ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_students = 0
for student in student_heights:
    total_students += 1


total_heights = 0
for height in student_heights:
    total_heights += height


Average_height = round(total_heights / total_students)
print(Average_height)