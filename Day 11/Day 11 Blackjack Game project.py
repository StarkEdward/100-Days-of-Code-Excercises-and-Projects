# blackjack game.
import random


# Function that deals the  random cards
def deal_card():
    """Returns a random card from a deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# function that calculate total score of cards.
def calculate_score(cards):
    """Take a list from cards and return the score calculated form cards"""
    if sum(cards) == 21 and len(cards) == 2:  # Blackjack if user or computer gets [11, 10] or [10, 11]
        return 0  # blackjack return as 0 so user know that its blackjack

    if 11 in cards and sum(cards) > 21:  # if in starting the users score gets more than 21  remove 11 and replace   with 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)  # return the total score of cards


# function that compare both user_score and computer_score
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "win with Blackjack"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You lose"


# function that is use to start a game
def play_game():


    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # Testing output of user_card & computer_card
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Press 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 or computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
