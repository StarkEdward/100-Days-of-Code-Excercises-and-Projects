from random import randint

# global constant
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# function to check  user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The Correct answer is: {answer}")
    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # let the user guess number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses. You Lose!")
            print(f"The correct answer is: {answer}")
            return
        elif guess != answer:
            print("Guess again")

game()
