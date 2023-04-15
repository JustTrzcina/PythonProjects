import os
import random
from game_data import data

clear = lambda: os.system('cls')

def get_next_item(previous_item):
    new_item = random.choice(data)
    if previous_item == new_item:
        new_item = random.choice(data)
    return new_item

def check_answer(guess, a_count, b_count): 
    if a_count > b_count:
        return guess =="a"
    else:
        return guess =="b"

def higher_lower():
    first_item = random.choice(data)
    player_score = 0
    didnt_loose = True

    while didnt_loose:
        print(f'Current score {player_score}.')
        next_item = get_next_item(first_item)

        scores = [first_item['follower_count'],next_item['follower_count']]
        print(f"Compare A: {first_item['name']}, {first_item['description']}, from {first_item['country']}")
        print("VS")
        print(f"Against B: {next_item['name']}, {next_item['description']}, from {next_item['country']}")
        player_decision = input("Who has more followers?, A/B: ").lower()
        if(check_answer(player_decision,scores[0],scores[1])):
            clear()
            print("You got it!")
            first_item = next_item
            player_score+=1
        else:
            clear()
            print("Unfortunately you were wrong.")
            if input("Do you want to continue? Y/N ").lower()=="n":
                clear()
                return
            else:
                player_score=0
                clear()
higher_lower()