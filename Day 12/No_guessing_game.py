from random import randint

# GLOBAL CONSTANTS
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
# function to check user's guess against actual answer and returns the nmbr of turns remaining.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! the answer was {answer}")

# set difficulty

def set_dificulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # choosing a random number btwn 1-100.
    print("Welcome to the Number Guessing Game.")
    print("Thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    print(f"the correct answer is {answer}")

    turns = set_dificulty()

    # repeat the gussing if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # let the user guess a number
        guess = int(input("Enter your guessed number: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're run out of guesses, You lose!")
            return  # this return statement stops the loop when no. of guesses ends.
        elif guess != answer:
            print("Guess again.")

game()
