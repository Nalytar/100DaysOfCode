from secret_auction_art import logo
from replit import clear


print(logo)
print("Welcome to the secret auction program.")

bidders = {}
highest_bidder = ""
highest_bid = 0
repeat_loop = True

while repeat_loop:
    auction_bidder = input("What is your name?: ")
    if auction_bidder in bidders:
        print("There is already a bidder with this name. You may want to specify yours!")
        continue

    bid = input("What's your bid? (Bid just whole numbers): $")
    if bid.isnumeric():
        bid = int(bid)
    else:
        print("Your bid wasn't a valid number!")
        continue

    bidders[auction_bidder] = bid

    repeat = input("Are there an other bidders? Type 'YES' or 'no'.\n").lower()
    if repeat == "no":
        repeat_loop = False

        for auction_bidder in bidders:
            if highest_bid < bidders[auction_bidder]:
                highest_bidder = auction_bidder
                highest_bid = bidders[auction_bidder]
    clear()

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
