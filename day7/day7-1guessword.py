# Check if the letter guessed comes in the word chosen randomly 

#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_words = random.choice(word_list)
# print(chosen_words)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()    # .lower() makes the string into lower case

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_words:
     if letter == guess:
         print("Right")
     else:
         print("Wrong")
    
