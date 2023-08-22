import random

from replit import clear
# this should clear our console
from blackjack_art import logo

# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] times four.
# Cards are removed from the deck as they are drawn.
# If the deck is empty, we add a new deck of cards.
# The computer is the dealer.


deck_of_cards = [
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

new_deck_of_cards = deck_of_cards.copy()
# Creating a sample deck to add cards from when our main deck is empty


def blackjack_start():
    print(logo)
    # empty Player Hands
    player_hand = []
    dealer_hand = []

    # Deal cards
    deal_cards(player_hand, dealer_hand)
    deal_cards(player_hand, dealer_hand)

    # Print first-state
    print_hands_without_second_dealer_card(player_hand, dealer_hand)

    # Check if player wants more cards,
    # busts, or got blackjack
    if not player_scored_blackjack(player_hand):
        while input("Type 'y' to get another card (hit), type any key to pass (stay): ").lower() == 'y':
            deal_to_player(player_hand)
            print_hands_without_second_dealer_card(player_hand, dealer_hand)
            if player_busts(player_hand):
                break

    # Reveal final hands
    check_for_winner_and_print_final_hand(player_hand, dealer_hand)
    print("\n-----------------------------------------------------\n")


def deal_cards(player, dealer):
    deal_to_player(player)
    deal_to_computer(dealer)


def deal_to_player(player):
    check_deck_size_and_add_cards()
    player.append(deck_of_cards.pop())
    check_if_ace_is_1_or_11(player)


def deal_to_computer(dealer):
    check_deck_size_and_add_cards()
    dealer.append(deck_of_cards.pop())
    check_if_ace_is_1_or_11(dealer)


def check_deck_size_and_add_cards():
    if len(deck_of_cards) < 1:
        for card in new_deck_of_cards:
            deck_of_cards.append(card)
        random.shuffle(deck_of_cards)


def print_hands_without_second_dealer_card(player, dealer):
    print(f"Your Cards: {player}\t Your Score: {sum(player)}")
    print(f"Dealer's first Card: {dealer[0]}\n")


def print_final_hand(player, dealer):
    print(f"Your final hand: {player}\t Your final score: {sum(player)}")
    print(f"Dealer's final hand: {dealer} \t Dealer's final score: {sum(dealer)}\n")


def player_busts(player):
    if sum(player) > 21:
        return True
    else:
        return False


def player_scored_blackjack(player):
    if sum(player) == 21 and len(player) == 2:
        return True
    return False


def check_for_winner(player, dealer):
    if sum(player) == 21 and len(player) == 2 and (sum(dealer) != 21 or len(dealer) != 2):
        print("Blackjack! You win! 😁")
    elif sum(player) == 21 and len(player) == 2 and sum(dealer) == 21 and len(dealer) == 2:
        print("2 Blackjack's?! 🤯 It's a draw! 😵")
    elif sum(player) > 21:
        print("You bust. You lose! 😢")
    elif sum(player) < sum(dealer) <= 21:
        print("You lose! 😢")
    elif sum(player) == sum(dealer):
        print("It's a draw! 😵")
    elif sum(player) <= 21 < sum(dealer):
        print("The Dealer bust. You win! 😁")
    elif sum(dealer) < sum(player) <= 21:
        print("You win! 😁")


def check_for_winner_and_print_final_hand(player, dealer):
    check_dealer_score_over_16(dealer)
    print_final_hand(player, dealer)
    check_for_winner(player, dealer)


def check_dealer_score_over_16(dealer):
    while sum(dealer) < 17:
        deal_to_computer(dealer)


def check_if_ace_is_1_or_11(hand):
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1


# --------------------------------------- Begin -------------------------------------------------
game_start = False
while not game_start:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    if want_to_play == "y":
        game_start = True
        random.shuffle(deck_of_cards)
        clear()
        blackjack_start()
    elif want_to_play == "n":
        exit()
    else:
        print("You didn't typed a valid input!")

while input("Do you want to play again? Type 'y' for another game, else press any key: ").lower() == "y":
    clear()
    blackjack_start()

# Project completed on difficult level Expert (day011.py)
# This was my to go for the solution I'm sure there are other better ways, but im pretty happy with how it came out
