# Dictionary Comprehension
# 1
# new_dict = {new_key : new_value for item in list}

# 2
# new_dict = {new_key : new_value for (key, value) in dict.items()}

# 3
# new_dict = {new_key : new_value for (key, value) in dict.items() if test}

###################################

# 1
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# 2
passed_students = {student : marks  for (student, marks) in students_scores.items() if marks >= 50}
print(passed_students)