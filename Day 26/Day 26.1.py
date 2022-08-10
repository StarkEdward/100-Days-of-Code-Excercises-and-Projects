# List Comprehension

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

# 2
name = "EDWARD"
new_word_list = [char for char in name]
print(new_word_list)

#
num_list = [num * 2 for num in range(1,5)]
print(num_list)

# conditional list comprehenslion
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_name = [name for name in names if len(name) < 5]
print(short_name)

upper_names = [name.upper() for  name in names if len(name) > 4]
print(upper_names)