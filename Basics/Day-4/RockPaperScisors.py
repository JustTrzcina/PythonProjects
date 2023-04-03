import random as ran
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
possibilities = [rock,paper,scissors]
outcomes = [["draw","win",'loose'],
            ["loose","draw","win"],
            ["win","loose","draw"]]

user_choice = input("Choose '1' for rock '2' for paper '3' for scissors:\n")
computer_choice = ran.randint(0,2)
user_choice_int = int(user_choice)-1
print(f"You:\n{possibilities[user_choice_int]}\nComputer:\n{possibilities[computer_choice]}")
print(f"You {outcomes[computer_choice][user_choice_int]}")