import os
def clear(): os.system('cls') #on Windows System
bidders = {}
are_bidders = True

print("Welcome to the auction house!")

while are_bidders:
    name = input("What is your name: \n")
    bid = input("How much would you like to bid: $")
    bidders[name]=bid
    more_bidders = (input("Are there any more bidders? yes -'Y', no - 'N'")).lower()
    if more_bidders =="y":
        clear()
    else:
        are_bidders=False

clear()
max_value = max(bidders.values())
max_bider = max(bidders,key=bidders.get)

print(f"{max_bider} wont the auction with ${max_value} bid")
