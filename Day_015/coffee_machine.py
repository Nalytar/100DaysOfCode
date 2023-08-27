"""
Coffee-Machine-Program
"""
__author__ = "Nalytar"
__version__ = "1.0.0"

from coffee_machine_resources import *


def coffee_machine_start():
    """
    Starts the Coffee-Machine program
    """
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    while True:
        # ToDo UserPrompt asking for coffee of their choice
        coffee_choice = input("What would your like? (espresso/latte/cappuccino)\n")
        coffee_choice = coffee_choice.lower()

        if coffee_choice == "off":
            turn_off()
        elif coffee_choice == "report":
            report_resources()
        elif coffee_choice in MENU.keys():
            if sufficient_resources(coffee_choice):
                insert_coins(coins)
                if check_transaction(coins, coffee_choice):
                    make_coffee(coffee_choice)
        print("\n--------------------------------------------------\n")


def turn_off():
    """
    Exits Program, 'Shuts Coffee-Machine down'
    """
    # ToDo 'off' as secret word to shutdown machine
    exit()


def report_resources():
    """
    Prints current resource-list and profit
    """
    # ToDo 'report' as secret word to print current resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def sufficient_resources(coffee_drink):
    """
    Checks if there are sufficient ingredients for the needed drink
    :param coffee_drink: Chosen Coffee drink by User
    :returns: True if enough provided, else False
    """
    # ToDo Check resources sufficient
    sufficient = True
    for ingredient in MENU[coffee_drink]["ingredients"]:
        if MENU[coffee_drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            sufficient = False
    return sufficient


def insert_coins(coins):
    """
    Checks for right input as integer
    :param coins: The coin dictionary to save user input
    """
    # ToDo Process coins
    print("Please insert coins.")
    quarters = input("How many quarters? ($0.25): ")
    while not quarters.isdigit():
        quarters = input("How many quarters? Please insert a integer! ($0.25): ")
    coins["quarters"] = int(quarters)

    dimes = input("How many dimes? ($0.10): ")
    while not dimes.isdigit():
        dimes = input("How many dimes? Please insert a integer! ($0.10): ")
    coins["dimes"] = int(dimes)

    nickles = input("How many nickles? ($0.05): ")
    while not nickles.isdigit():
        nickles = input("How many nickles? Please insert a integer! ($0.05): ")
    coins["nickles"] = int(nickles)

    pennies = input("How many pennies? ($0.01): ")
    while not pennies.isdigit():
        pennies = input("How many pennies? Please insert a integer! ($0.01): ")
    coins["pennies"] = int(pennies)


def check_transaction(coins, coffee):
    """
    Checks if user inserts enough coins
    :param coins: inserted coins in a dictionary
    :param coffee: coffee drink chosen by user
    :returns: False if inserted not enough coin values, else True
    """
    # ToDo Check transaction successful
    # get money from coffee_machine_resources
    global money
    inserted_money = ((coins["quarters"] * 0.25) +
                      (coins["dimes"] * 0.10) +
                      (coins["nickles"] * 0.05) +
                      (coins["pennies"] * 0.01))
    if MENU[coffee]["cost"] > inserted_money:
        print("\nSorry that's not enough money. Money refunded.\n")
        return False
    else:
        change = inserted_money - MENU[coffee]["cost"]
        money += MENU[coffee]["cost"]
        print(f"\nYour change: ${change:.2f}\n")
        return True


def make_coffee(coffee_choice):
    """
    :param coffee_choice: The chosen coffee drink by the user
    Reduces all resources by the value of the needed ingredients
    """
    # ToDo Make Coffee
    for ingredient in MENU[coffee_choice]["ingredients"]:
        resources[ingredient] -= MENU[coffee_choice]["ingredients"][ingredient]
    print(f"Here is your {coffee_choice}. Enjoy! ☕")


# Some of these docstrings seems unnecessary, I just wanted to play a bit around with this
coffee_machine_start()
