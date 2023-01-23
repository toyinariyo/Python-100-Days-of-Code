import os
from art import logo

def cls():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
bids = {}  # Create an empty dictionary for the bids
bidding_finished = False  # Create a boolean for when the bidding has finished


def find_highest_bidder(bidding_record):  # Argument for the bids empty dictionary
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Going once! Going twice! Sold to {winner} with a bid of £{highest_bid}")


while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("How much are you bidding? £"))
    bids[name] = price
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_bidding == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif continue_bidding == "yes":
        cls()
