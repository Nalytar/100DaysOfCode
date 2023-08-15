import random
# without error-handling if user types in "hello world"

print('''
┏━━━┓━━━━━━━━┏┓━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━━
┃┏━┓┃━━━━━━━━┃┃━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━━━━━━
┃┗━┛┃┏━━┓┏━━┓┃┃┏┓━━━━┃┗━┛┃┏━━┓━┏━━┓┏━━┓┏━┓━━━━┃┗━━┓┏━━┓┏┓┏━━┓┏━━┓┏━━┓┏━┓┏━━┓
┃┏┓┏┛┃┏┓┃┃┏━┛┃┗┛┛━━━━┃┏━━┛┗━┓┃━┃┏┓┃┃┏┓┃┃┏┛━━━━┗━━┓┃┃┏━┛┣┫┃━━┫┃━━┫┃┏┓┃┃┏┛┃━━┫
┃┃┃┗┓┃┗┛┃┃┗━┓┃┏┓┓━━━━┃┃━━━┃┗┛┗┓┃┗┛┃┃┃━┫┃┃━━━━━┃┗━┛┃┃┗━┓┃┃┣━━┃┣━━┃┃┗┛┃┃┃━┣━━┃
┗┛┗━┛┗━━┛┗━━┛┗┛┗┛━━━━┗┛━━━┗━━━┛┃┏━┛┗━━┛┗┛━━━━━┗━━━┛┗━━┛┗┛┗━━┛┗━━┛┗━━┛┗┛━┗━━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

user_input = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
com_input = random.randint(0, 2)

if 0 <= user_input < 3:
    print(choices[user_input])
    print("Computer chose:")
    print(choices[com_input])

    if user_input == 0 and com_input == 1:
        print("You lose")
    elif user_input == 0 and com_input == 2:
        print("You win")
    elif user_input == 1 and com_input == 0:
        print("You win")
    elif user_input == 1 and com_input == 2:
        print("You lose")
    elif user_input == 2 and com_input == 0:
        print("You lose")
    elif user_input == 2 and com_input == 1:
        print("You win")
    else:
        print("It's a draw")
else:
    print("Invalid number")
