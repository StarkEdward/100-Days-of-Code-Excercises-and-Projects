# Blind Auction Program
import os
import art

print(art.logo)
print("Welcome to the Secret Auction Program.")

bidder_record = {}


def find_highest_bidder(bid):
    highest_bid = 0
    winner = ""
    for bidder in bid:
        bid_amount = bid[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ₹{highest_bid}.")


while True:
    name = input("What is your name: ")
    price = int(input("What's your bid amount: ₹"))
    bidder_record[name] = price
    choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if choice == 'no':
        find_highest_bidder(bid=bidder_record)
        break
