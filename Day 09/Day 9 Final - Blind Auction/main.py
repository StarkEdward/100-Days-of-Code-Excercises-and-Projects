# Blind Auction Program
import os
import art

print(art.logo)
print("Welcome to the Secret Auction Program.")

bidder_record = {} # Creating an empty Dict to keep track of entries,

# Creating function to find out highest bidder and winner name.
def find_highest_bidder(bid):
    highest_bid = 0
    winner = ""
    for bidder in bid:
        bid_amount = bid[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ₹{highest_bid}.")    #Disply the final output


while True:
    name = input("What is your name: ")
    price = int(input("What's your bid amount: ₹"))
    bidder_record[name] = price
    choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if choice == 'no':
        find_highest_bidder(bid=bidder_record)      # calling the function
        break
    else:
        os.system("cls")        # clear the screen for Windows
    #     os.system("clear")      # clear the screen for Linux