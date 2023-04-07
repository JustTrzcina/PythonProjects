#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = word_list[random.randint(0,len(word_list)-1)]
print(random_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
chosen_letter = input("Choose a letter: ")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if chosen_letter in random_word:
    print(f"You got it, there is a '{chosen_letter}' in this word")