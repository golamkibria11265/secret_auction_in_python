from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False


def highest_bidder(table):
    highest_bid = 0
    winner = ""
    for bidder_name in table:
        bid_value = int(table[bidder_name])
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder_name
    print(f"The winner is ${winner} with ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?\n")
    bid = input("What is your bid price in $?\n")
    bids[name] = bid
    another = input("Is there any other person to bid?\n").lower()
    if another == "yes":
        clear()
    elif another == "no":
        bidding_finished = True
        highest_bidder(bids)
