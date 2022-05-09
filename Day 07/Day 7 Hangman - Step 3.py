import random

# step 3

word_list = ["elephant", 'horse', 'camel', 'baboon']
chosen_word = random.choice(word_list)

print("Solution is : ", chosen_word)
word_length = len(chosen_word)
# create blanks
display =[]
for _ in range(word_length):
    display += "_"

print(display)

# TODO - 1 - use while loop to let theruser guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks("_"). Then ou can tell the user they've won.

end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current Position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")

        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_game = True
        print("You Won!")

