from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

# function to check the user's guess against actual number

turns = 0

def check(guess, answer, turns):
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You guessed it right.The number was {answer}")

# make a function to set difficulty


def set_difficulty():
    level = input(
        "Choose the level at which you want to play the game, 'easy' or 'hard'? ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("Welcome to the number guessing game.")
    print("Thinking of a number btwn 1-100")

    answer = randint(1, 100)
    print(f"the correct answer is {answer}")

    # track the number of turns and reduce it if they get it wrong
    turns = set_difficulty()

    # repeat the gussing if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts left")

        # let the user guess a number
        guess = int(input("Guess a number: "))

        turns = check(guess, answer, turns)
        if turns == 0:
            print("You're run out of guesses, You lose!")
            # this return statement stops the loop when no. of guesses ends.
            return
        elif guess != answer:
            print("Guess again.")


game()
