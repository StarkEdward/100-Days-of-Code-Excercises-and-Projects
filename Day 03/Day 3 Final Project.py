print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You\'re at a crossroad. Where do you want to go? Type 'left' or 'right'.\n").lower()
if choice1 == 'left':
  print("You\'ve come to lake. There is an Island in the middle of the lake.")
  choice2= input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
  if choice2 == 'wait' or choice2 == 'Wait' or choice2 == 'WAIT':
    print("You arrive at the island unharmed.\nThere is 3 doors. One red, one yellow and one blue.")
    choice3 = input("Which colour do you choose?\n").lower()
    if choice3 == 'red':
      print("It\'s a room full of fire, You burned to death.\nGame Over!")
    elif choice3 == 'yellow':
      print("You found the Treasure!\nYou Win!")
    elif choice3 == 'blue':
      print("You enter the room of Monsters.\nGame Over!")
    else:
      print("You chose a door that doesn\'t exist.\nGame Over.")
  else:
    print("Attacked by Crocodile.\nGame Over!")
else:
  print("You Fall into a hole.\nGame Over!")

