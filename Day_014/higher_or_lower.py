from higher_or_lower_art import *
from game_data import *
import replit
import random


def higher_or_lower_start():  # basically using a do-while loop in python style
    replit.clear()
    print(logo)
    # get Random Compare Objects
    score = 0
    compare_a = random.choice(data)
    compare_b = check_b_not_equals_a(compare_a)
    # print
    print_comparing_objects(compare_a, compare_b)
    # get input
    choose_right, right_answer = compare_follower(compare_a, compare_b)

    while choose_right:
        score += 1
        replit.clear()  # since replit don't work in pycharm console, I use the next line for clear separation
        print("\n----------------------------------------------------------------------\n")
        print(logo)
        print(f"You're right! Current score: {score}")
        compare_a = right_answer
        compare_b = check_b_not_equals_a(compare_a)
        print_comparing_objects(compare_a, compare_b)
        choose_right, right_answer = compare_follower(compare_a, compare_b)

    print("\n----------------------------------------------------------------------\n")
    print(f"Sorry that's wrong. Final score: {score}")


def print_comparing_objects(compare_a, compare_b):
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")


def compare_follower(compare_a, compare_b):
    user_guess = user_guessing()

    if compare_a['follower_count'] > compare_b['follower_count'] and user_guess == 'A':
        return True, compare_a
    elif compare_a['follower_count'] < compare_b['follower_count'] and user_guess == 'B':
        return True, compare_b
    elif compare_a['follower_count'] == compare_b['follower_count']:
        if user_guess == 'A':
            return True, compare_a
        else:
            return True, compare_b
    else:
        return False, None


def user_guessing():
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    while user_guess != 'A' and user_guess != 'B':
        user_guess = input("Please Type in 'A' or 'B': ").upper()
    return user_guess


def check_b_not_equals_a(compare_a):
    compare_b = random.choice(data)

    while compare_a == compare_b:
        compare_b = random.choice(data)
    return compare_b


# ----------------------------------- Begin -----------------------------------
higher_or_lower_start()

play_again = input("Want to play another round? Type 'yes' else press any key: ").lower()

while play_again == "yes":
    higher_or_lower_start()
    play_again = input("Want to play another round? Type 'yes' else press any key: ")
