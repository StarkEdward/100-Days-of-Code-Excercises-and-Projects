from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


# function to check  user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too High.")
    elif guess < answer:
        print("Too low")
    else:
        print("You got it! The answer was {answer}")


# make function to set difficulty
def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        print(f"You have {EASY_LEVEL} attempts remaining to guess the number.")
    else:
        print(f"You have {HARD_LEVEL} attempts remaining to guess the number")


# Choosing a random number between 1 and 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"The Correct answer is: {answer}")

# let the user guess number
guess = int(input("Make a guess: "))

# Track the number of urns and reduce by 1 if they get it wrong.

# Repeat the guessng functionality if they get it wrong.
