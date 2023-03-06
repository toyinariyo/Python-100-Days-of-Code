# Scope

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")  # Enemies equals 2 because enemies variable is assigned 2 inside
#     # increase_enemies function (local scope)
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}") # Enemies equals 1 because enemies variable is assigned 1 outside function
# # (global scope)

# Number Guessing Game
from art import logo
from random import randint

EASY_MODE = 10
HARD_MODE = 5


# Check user's guess against answer
def check_user_answer(guess, answer, turns):
    if guess > answer:
        print("You guessed too high.")
        return turns - 1
    elif guess < answer:
        print("You guessed too low.")
        return turns - 1
    else:
        print(f"You guessed correctly! The answer was {answer}")


# Set difficulty
def set_difficulty():
    level = input("To choose an easy difficulty, type easy. To choose a hard difficulty, type hard: ")
    if level == "easy":
        return EASY_MODE
    else:
        return HARD_MODE


def game():
    print(logo)
    # Select random number between 1 and 100 with random module
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"The correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    # Repeat guessing functionality if user guesses the wrong number
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the correct number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_user_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
