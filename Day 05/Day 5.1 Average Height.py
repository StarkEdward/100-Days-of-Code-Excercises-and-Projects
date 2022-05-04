student_heights = input("Input a list of student heihts ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
number_of_students = n + 1
for add in student_heights:
    total += add
Average_height = round(total / number_of_students)
print(Average_height)