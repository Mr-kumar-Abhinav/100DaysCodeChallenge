from art import logo, vs
from game_data import data
import random
import os

# 👇Takes the user guess and follower count and returns if they got it right.
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
# format the account data in printable format.
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Making the game repeatable:
while game_should_continue:
    # Generate a random accunt from the game_data
    account_a = random.choice(data)
    # Making account at position B become the account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data) # regenerating account_b if both the accounts are same.

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess:
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)
    #  Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You'r right! Your current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, You got it wrong! Final score is {score}")