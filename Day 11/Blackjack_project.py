import random
import os
from art import logo

# hint4 - Create a deal_card() function that uses the List below to *return* a random card.


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

# hint6 - it takes a List of cards as input and returns the score.


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:  # hint7 - logic of blackjack
        return 0
    if 11 in cards and sum(cards) > 21:  # hint8 - logic for checking ace
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw...


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"


    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over, You lose."
    elif computer_score > 21:
        return"Opponent went over. You win."
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose."


def play_game():

    print(logo)
    # hint5 - Deal the user and computer 2 cards each using deal_card()
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    # Hint11: 1st while loop created for the user to play. The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        # hint9 - call the calculate_score function
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # hint10 - If the game has not ended, ask the user if they want to draw another card.
            user_should_deal = input(
                "type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    # hint12 - 2nd while loop created is for the computer. it's time to let the computer play.
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Hint14: Ask the user if they want to restart the game.


while input("Do you want to play a game of blackjack? type 'y' or 'n': "):
    os.system('cls')
    play_game()
