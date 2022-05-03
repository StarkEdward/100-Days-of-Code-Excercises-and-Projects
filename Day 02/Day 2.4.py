#Date: 21-Dec-2021     Coading excercise   @Sagar Kamble
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 135, then the output should be 1 + 3 + 5 = 8

three_digit_num = input("Enter three digit Number: ") #input is in form of string "135"

num_1 = int(three_digit_num[0]) #convert str to int and subscript [0] is calling 1
num_2 = int(three_digit_num[1]) #convert str to int and subscript [1] is calling 3
num_3 = int(three_digit_num[2]) #convert str to int and subscript [2] is calling 5

result = num_1 + num_2 + num_3  # result = 1 + 3 + 5

print(f"The addtion of 3 digit number is: {num_1} + {num_2} + {num_3} = {result}")   #prints the final output = 9
