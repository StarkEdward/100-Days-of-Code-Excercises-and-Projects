from random import randint

# global constant
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# function to check  user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too High.")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}")


# make function to set difficulty
def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Choosing a random number between 1 and 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"The Correct answer is: {answer}")

# let the user guess number
guess = int(input("Make a guess: "))
turns = check_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")
# Track the number of urns and reduce by 1 if they get it wrong.

# Repeat the guessng functionality if they get it wrong.
