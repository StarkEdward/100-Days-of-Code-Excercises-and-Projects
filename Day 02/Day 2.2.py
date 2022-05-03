# Date: 21-Dec-2021                 @Sagar Kamble
#Day 2.2 Excercise: Create a Simple BMI Calculator

print("Welcome to the BMI(Body Mass Index Calculator.)\n")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
print("Your BMI is :", int(bmi))    #output is in whole number (int used)
