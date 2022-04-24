# Randomly choose a word from the word_list and assign it to a variable called choosen_word. 

import random
from stages import *
import os

print(logo)

end_of_game = False
word_list = ["kumar", "abhinav", "Anshu", "saloni", "roshni"]
chosen_word = random.choice(word_list)

lives = 6

# creat an empty list called display and for each letter in the chosen_word, add a "_" to "display". 
# create blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"

# Ask the user to guess the letter and assign their ans to a variable called guessed_letter & make it lowercase.

# check if the letter the user guessed is one of the letters in the chosen_word

# loop through each position in the chosen_word, if the letter at that position matches 'guess' then reveal that letter in the display at that position.

# use a while loop to let the user guess again. the loop should only stop once the user has guessed all the letters in the chosen_word and if "display" has no more blanks, then tell the user that they won.

while not end_of_game:
    guessed_letter = input("Guess a letter to check: ").lower()

    os.system('cls')

    # if the user has entered a letter they have already guessed, print the letter and let them know.

    if guessed_letter in display:
        print(f"You'hv already guessed {guessed_letter}")

    # check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guessed_letter}")
        if letter == guessed_letter:
            display[position] = letter        

# reducig the lives of man if the guessed_letter is not in the chosen_word.
    if guessed_letter not in chosen_word:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose the game😑😞")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")


    # check if user got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win this game🎉🤗")


    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])