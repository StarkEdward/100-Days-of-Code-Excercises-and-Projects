

#Write your code below this line 👇
print("Welcome to the tip Calculator.")
bill = float(input("What was the total bill? ₹ "))
tip = float(input("What Percentage(%) tip would you like to give? 7, 10, 12, 15 = "))
people = int(input("How many peope to split the bill? "))

new_amount = bill + (bill * (tip / 100))

bill_split = round(new_amount / people, 2)

print(f"Each person should pay: ₹ {bill_split}")
print("Thank you for using tip calculator!\nHave a nice day!")
