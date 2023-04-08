#Step 1 
import random
import word_list as wl
word_list = wl.word_list
tries = 6

random_word = word_list[random.randint(0,len(word_list)-1)]
word_length = len(random_word)
guessed_word = []
used_characters=[]
for letter,x in zip(random_word,range(len(random_word))):
    guessed_word.append("_") 
print(random_word)
while ''.join(guessed_word) != random_word and tries !=0:
    chosen_letter = input("Choose a letter: ")
    if chosen_letter in random_word:
        for index,letter in zip(range(word_length),random_word):
            if chosen_letter == random_word[index]:
                guessed_word[index]=chosen_letter
        used_characters.append(chosen_letter)
        print(f"There was '{chosen_letter}' letter in this word")
        print("Current guessed words "+ " , ".join(guessed_word))
        print("Current used characters "+ " , ".join(used_characters))
    else:
        used_characters.append(chosen_letter)
        tries -=1
        print(f"There is no '{chosen_letter}' in this word, you have {tries} more tries")
        print("Current guessed words "+ " , ".join(guessed_word))
        print("Current used characters "+ ",".join(used_characters))
if tries > 0:
    print(f"Congratulations you won! The word was {random_word}")
else:
    print("You loose")

