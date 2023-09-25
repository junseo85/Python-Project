from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

auction = {}
blind_auction = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not blind_auction:
    user_input = input("What is your name?: ")
    bid_price = int(input("What's your bid?:  $"))
    auction[user_input] = bid_price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if other_bidders == "no":
        blind_auction = True
        find_highest_bidder(auction)
    elif other_bidders == "yes":
        clear()


