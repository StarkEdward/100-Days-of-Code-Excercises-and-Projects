import os
import random
from art import logo, vs
from game_data import data


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


# Display art
print(logo)

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format.
print(f"Compare A : {format_data(account_a)}")
print(f"Against B: {format_data(account_b)}")

# Ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()
# check is user is correct

## Get follwer count of each account.
## Use if statemnt to check if user is correct.

# Give user feedback on their guess.

# Score keeping

# Make the game repeatable

# Making account at position B become the next account at position A

# Clear the screen between rounds.