# new_users = True

# while new_users:

#     name = input("Enter the name of the bidder: ")
#     bid_price = int(input("Enter the bidding price: "))

#     bidders_dict = {
#         f"{name}": f"{bid_price}"
#     }
import os

bids = {}
bidding_finished = False
winner = ""


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name: ")
    price = int(input("what is your bid? $"))

    # adding name and bid into a dictionary as key:value pair.
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
