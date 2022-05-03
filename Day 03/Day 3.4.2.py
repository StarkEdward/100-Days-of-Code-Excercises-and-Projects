
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


bill = 0

if size == 's' or size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2
    if extra_cheese == 'Y':
      bill += 1
      print(f"Your final bill is {bill}")
    else:
      print(f"Your final bill is {bill}")
  else:
    print(f"Your final bill is {bill}")
elif size == 'M' or size == 'm':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3
    if extra_cheese == 'Y':
      bill += 1
      print(f"Your final bill is {bill}")
    else:
      print(f"Your final bill is {bill}")
  else:
    print(f"Your final bill is {bill}")
else:
  bill = 25
  if add_pepperoni == 'Y':
    bill += 3
    if extra_cheese == 'Y':
      bill += 1
      print(f"Your final bill is: ${bill}")
    else:
      print(f"Your final bill is: ${bill}")
  else:
    print(f"Your final bill is: ${bill}")






