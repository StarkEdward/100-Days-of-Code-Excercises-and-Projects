# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


new_name = (name1 + name2).lower()
T = new_name.count('t')
R = new_name.count('r')
U = new_name.count('u')
E = new_name.count('e')
true = T + R + U + E
L = new_name.count('l')
O = new_name.count('o')
V = new_name.count('v')
E = new_name.count('e')
love = L + O + V + E
score = str(true) + str(love)
score = int(score)
if score < 10 or score > 90:
  print(f"Your love score is {score}%, You go together like coke and mentos.")
elif score >=40 and score <= 50:
  print(f"Your love score is {score}%, You are alright together.")
else:
  print(f"Your love score is {score}%")

