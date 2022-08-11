# Iterate over a pandas database
import pandas

student_dict = {
    "student": ["Edward", "Jarvis", "Friday",],
    "score": [75,55,68]
}

#Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

###############

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, val) in student_data_frame.items():
#     print(key)
#     print(val)

# inbuilt loop in pandas
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "Edward":
        print(row.score)