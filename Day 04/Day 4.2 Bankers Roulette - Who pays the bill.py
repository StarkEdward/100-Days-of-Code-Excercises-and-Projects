import random

names  = input("enter your friends names, separeted by comma.: ").split(", ")

# using random.choice()
# pay_bill = random.choice(names)
# print(f"{pay_bill} is goint to pay the bill.")
########
# using randint() method
num_item = len(names)
pay_bill = random.randint(0, num_item -1)
print(f"{names[pay_bill]} is going to pay the bill.")