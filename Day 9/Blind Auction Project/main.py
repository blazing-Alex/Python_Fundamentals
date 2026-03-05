# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
import os

print(logo)

def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner}, with a bid of ${highest_bid}")

bid_list = {}
continue_bidding = True

while continue_bidding:
    user_name = input("Enter your name: \n")
    user_bid = int(input("Enter your bid: $"))
    bid_list[user_name] = user_bid
    should_continue = input("Would you like to continue (y/n)? \n").lower()
    if should_continue == "n":
        continue_bidding = False
        find_highest_bid(bid_list)
    elif should_continue == "y":
        os.system("cls")




