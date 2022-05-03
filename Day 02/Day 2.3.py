#Date: 22-Dec-2021  *Interative Coading Excercise*  @Sagar Kamble
'''Write a program that tells us how many days, weeks and months
   we have left if we live until 90 years old.'''

print("\t\tWelcome to the Program")
print("Lets see how many days, weeks and months left\nif you live until 90 years old.\n")

age = input("What is your current age? ")

days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
months = (90 - int(age)) * 12

print(f"\nYou have {days} days, {weeks} months, {months} Months left.")

