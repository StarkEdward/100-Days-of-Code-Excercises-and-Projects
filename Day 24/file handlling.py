# we can read and write a file

# # reading file
# file = open("my_file.txt")  # to open the file
# contents = file.read()  # to read teh file
# print(contents)  # display file content.
# file.close()  # use to close file

# 2nd method
with open("my_file.txt") as file:       #
    contents = file.read()
    print(contents)

# # Writing a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nnew Text here.")

# with open("test.txt", mode="w") as file:            # only works with write mode.
#     file.write("Hello This a example to create a new file and write automatically in it.")


