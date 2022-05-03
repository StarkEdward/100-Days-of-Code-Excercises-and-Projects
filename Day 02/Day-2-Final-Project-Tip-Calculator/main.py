#Date: 22-Dec-2021      Day 2. Final Project       @Sagar Kamble
#Project Name: Create a program to calculate total bill with tip and split the bill in equal amount.
print("Welcome to the tip Calculator.")
bill = float(input("What was the total bill? ₹ "))
tip = float(input("What Percentage(%) tip would you like to give? 7, 10, 12, 15 = "))
people = int(input("How many peope to split the bill? "))

bill_with_tip = bill + (bill * (tip / 100))
bill_split = round(bill_with_tip / people, 2)

print("The total bill with tip is: ₹ {:.2f}".format(bill_with_tip))
print("Each person should pay: ₹ {:.2f}".format(bill_split))
print("Thank you for using tip calculator!\nHave a nice day!")
