
print("Welcome to the tip Calculator.")
bill = float(input("What was the total bill? ₹ "))
tip = float(input("What Percentage(%) tip would you like to give? 7, 10, 12, 15 = "))
people = int(input("How many peope to split the bill? "))

bill_with_tip = bill + (bill * (tip / 100))
bill_split = round(bill_with_tip / people, 2)
#"{:.2f}".format() is used to double precision eg- 30.6 to 30.60
bill_with_tip = "{:.2f}".format(bill_with_tip)
bill_split = "{:.2f}".format(bill_split)

print(f"The total bill with tip is: ₹{bill_with_tip}")
print(f"Each person should pay: ₹ {bill_split}")
print("Thank you for using tip calculator!\nHave a nice day!")
