import random

print("Welcome to the number guessing game guessing game")
difficulty = input("Choose the difficulty level '1' - easy, '2' - hard: ")
if  difficulty=="1":
    number_of_tries = 10;
elif difficulty=="2":
    number_of_tries = 5;
else:
    print("Wrong input, shutting down.")


def guessing(tries:int):
    random_number = random.randint(1,100)
    print(f"You have {tries} to guess correctly")
    while tries > 0 :
        guess = int(input("Guess a number: "))
        if guess == random_number:
            return(f"You guessed right! The number was {guess}")
        elif guess > random_number:
            print(f"Your guess of {guess} was too high.")
        else:
            print(f"Your guess of {guess} was to low")
        tries -=1;
        print(f"You have {tries} more tries.")
    return print(f"You ran out of tries, the hidden number was {random_number}")


guessing(number_of_tries)
