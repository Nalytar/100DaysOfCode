from number_guessing_game_art import logo
from replit import clear
import random

MODES = {
    "hard": 5,
    "medium": 7,
    "easy": 10
}


def game_start():
    clear()
    print(logo)
    # Generate new number and get difficulty
    number_to_guess = random.randint(1, 100)
    attempts = get_difficulty_attempts()
    # Game-loop
    while attempts > 0 and game_round(attempts_remaining=attempts, number_to_guess=number_to_guess):
        attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    print("\n----------------------------------------------------\n")


def get_difficulty_attempts():
    difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
    while difficulty not in MODES.keys():
        difficulty = input("Please Enter a valid difficulty. Type 'easy', 'medium' or 'hard': ")
    return MODES[difficulty]


def game_round(attempts_remaining, number_to_guess):
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    guessed_number = user_guessed_number_input()
    if not check_for_hit(guessed_number=guessed_number, number_to_guess=number_to_guess):
        return True
    return False


def user_guessed_number_input():
    user_number = input("Make a guess: ")
    while not user_number.isdigit():
        user_number = input("Please type in a integer number: ")
    return int(user_number)


def check_for_hit(guessed_number, number_to_guess):
    if guessed_number > number_to_guess:
        print("Too high.")
    elif guessed_number < number_to_guess:
        print("Too low.")
    if guessed_number == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}")
        return True
    return False


game_start()
while input("Type 'yes' for another round, else press any key: ").lower() == "yes":
    game_start()
