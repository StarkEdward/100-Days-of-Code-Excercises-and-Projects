# Blind Auction Program
import os
import  art

print(art.logo)
print("Welcome to the Secret Auction Program.")

all_record = []

def add_new_record(bidder_name, bidding_amount):
    data = {}


name = input("What is your name: ")
bid = int(input("What's your bid amount: ₹"))

add_new_record(bidder_name=name, bidding_amount=bid)
