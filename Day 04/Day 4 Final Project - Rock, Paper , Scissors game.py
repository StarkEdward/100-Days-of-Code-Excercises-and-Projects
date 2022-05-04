# day 4 Final Project : Rock Paper Scissors game
import random
rock = '''
    _______
---'   ____ )
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____ )____
          ______ )
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____ )____
          ______ )
       __________)
      (____)
---.__(___)
'''

rps =[rock, paper, scissors]
user = int(input("What do you Choose?\nType 0 for Rock, 1 for Paper or 2 for scissors: "))

if user > 3 and user < 0:
    print("Invalid Choice, You Lose!")
else:
    print(rps[user])
    bot = random.randint(0, 2)
    print(rps[bot])
    if user == 0 and bot == 2:
        print("You Win!")
    elif bot == 0 and user == 2:
        print("You Lose!")
    elif user > bot:
        print("You Win!")
    elif user < bot:
        print("You Lose!")
    elif user == bot:
        print("Its Draw!")