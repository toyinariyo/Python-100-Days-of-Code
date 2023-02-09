# Hint 4: Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
import random
import os
from art import logo


def cls():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


# Hint 4: Create a function called deal_card() that uses a list to return a random card. 11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


# Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score.
def calculate_score(cards):
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0.
    # 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace).
    # If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over 21. You lose."
    if player_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Computer has Blackjack."
    elif player_score == 0:
        return "Congratulations, you got a Blackjack!"
    elif player_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."


def play_game():
    print(logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    player_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    # Hint 11: The score will need to be rechecked with every new card drawn.
    # The checks in Hint 9 need to be repeated until the game ends.
    while not game_over:
        # Hint 9: Call calculate_score().
        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, your current score is: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card.
            # If yes, then use the deal_card() function to add another card to the user_cards List.
            # If no, then the game has ended.
            player_deals_again = input("Type 'y' to get another card or type 'n' to pass: ")
            if player_deals_again == "y":
                player_cards.append(deal_card())
            else:
                game_over = True
        # Hint 12: Once the user is done, it's time to let the computer play.
        # The computer should keep drawing cards as long as it has a score less than 17.
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        print(f"Your final hand: {player_cards}, your final score is: {player_score}")
        print(f"Computer's final hand: {computer_cards}, computer's final score is: {computer_score}")
        print(compare(player_score, computer_score))


# Hint 14: Ask the player to restart the game.
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == "y":
    cls()
    play_game()
