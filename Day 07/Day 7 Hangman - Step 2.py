import random

# step 2
word_list = ["elephant", 'horse', 'camel', 'baboon']
chosen_word = random.choice(word_list)

# testing code
print(f"The solution is {chosen_word}")

# TODO-1 - Create an empty list called display.
# for each letter in the chosen_word, add a "_" to 'display'
# so in the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

# TODO-2 - Loop through each postion in the chosen wrod.
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] += letter


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)

#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
