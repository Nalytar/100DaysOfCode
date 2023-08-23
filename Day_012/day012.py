# udemy Course - 100 Days of Code - Python

# Scope ---

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope ---
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
# print(potion_strength) variable potion_strength is only available in drink_potion

player_health = 10  # global variable


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()
print(player_health)

# There is no Block Scope ---
if 3 > 2:
    a_variable = 10

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]


# print(new_enemy)  # not in the bound of the function

# Modifying Global Scope ---

enemies = 1


def increase_enemies():
    global enemies  # confusing, makes things easier to fail, avoid modifying global scope in functions
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159  # all in uppercase
URL = "https://www.google.de"


def print_pi():
    print(PI)
