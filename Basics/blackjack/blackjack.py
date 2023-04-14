import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
should_continue=True


def get_cards(amount:int, deck:list):
    for x in range(amount):
        deck.append(cards[random.randint(0,len(cards)-1)])
    return deck

def get_deck_sum(deck:list):
    deck_sum = sum(deck)
    if deck_sum > 21 and 11 in deck:
        ace_position = deck.index(11)
        deck[ace_position]=1
        return sum(deck)
    return deck_sum


def blackjack():
    draw_cards = True
    user_hand=[]
    house_hand=[]

    user_hand=get_cards(2,user_hand)
    house_hand=get_cards(1,house_hand)
    print("--------")
    print(f"Your hand: {user_hand}\nHouse hand: {house_hand}")
    house_hand=get_cards(1,house_hand)
    while draw_cards:
        if input("Do you want to draw another card? Y/N: ").lower()=="y":
            user_hand=get_cards(1,user_hand)
            print(f"Your current hand {user_hand} with sum of {get_deck_sum(user_hand)}")
        else:
            draw_cards=False
    if get_deck_sum(house_hand)<17:
        house_hand=get_cards(1,house_hand)
    house_sum=get_deck_sum(house_hand)
    user_sum=get_deck_sum(user_hand)
    print(f"\nYour current hand {user_hand} with sum of {user_sum}")
    print(f"House's current hand {house_hand} with sum of {house_sum}")
    if house_sum>21:
        print("House went over 21, you win!")
    elif user_sum>21:
        print("You went over 21, house wins.")
    elif user_sum>house_sum:
        print("You have more points than the house, You win!")
    else:
        print("House wins.")
    print("--------")


while should_continue:
    blackjack()
    if input("Do you want to play another game? Y/N").lower()=="n":
        should_continue = False