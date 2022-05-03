# Date : 20-Dec-2021       Coading Excersise           @Sagar Kamble
# Program for finding the length of typed name. (Example 1)

print("Welcome!\n") # Greeting Message 

f_name = input("Enter the First Name = ")  #variable1
l_name = input("Enter the Last Name =  ")  #variable2
length = f_name + l_name   #variable3 = variable1 + variable2 

print("\nHello " + f_name + " " + l_name)   #prints the f_name & l_name.
print("\nNo of characters in you Name is : ") 
print(len(length), "Letters")   # output gives the length.