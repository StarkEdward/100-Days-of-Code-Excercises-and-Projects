
#Write your code below this line 👇
print("Welcome to the tip Calculator!")
total_bill = input("What was the total bill? ₹ ")
percentage_tip = input("What Percentage(%) tip would you like to give? 7, 10, 12, 15 = ")
people = input("How many peope to split the bill? ")

t_bill_float = float(total_bill)
percent_tip_int = round(float(percentage_tip))
people_int = int(people)

new_amount = t_bill_float + (t_bill_float * (percent_tip_int / 100))

bill_split = round(new_amount / people_int, 2)

print(f"Each person should pay: ₹ {bill_split}")
print("Thank you for using tip calculator.\nHave a nice day!")
