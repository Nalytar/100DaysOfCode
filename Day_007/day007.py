# udemy Course - 100 Days of Code - Python
import random
import hangman_art as art
import hangman_wordlist as word_list
from replit import clear

player_life = len(art.stages)
# word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list.word_list)
display = []
for letter in chosen_word:
    display.append("_")

print(art.logo)

end_of_game = False

while not end_of_game:

    guess = input("Insert a letter: ").lower()
    clear()

    if guess in display:
        print(f"\nYou already guessed {guess}")
        print("----------------------------------------\n")
        continue

    if guess in chosen_word:
        for position in range(0, len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(art.stages[player_life - 1])
        player_life -= 1
        if player_life == 0:
            end_of_game = True
            print("You lose")
            print(f"The word we were looking for was: {chosen_word}")
            break

    print(f"\n{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won")
