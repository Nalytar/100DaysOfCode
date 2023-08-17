# udemy Course - 100 Days of Code - Python

# functions
# def function_name():
#   print("indentation is important")


# indentation
# is important to define what is inside the code block of various elements like
# if, for, while or for function body's

# -----------------------------------------------------------------------------------

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdle 1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for _ in range(1,5):
#     jump()

# -----------------------------------------------------------------------------------

# - while loop
# Hurdle 2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal:
#   jump()

# -----------------------------------------------------------------------------------

# Hurdle 3

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#   if front_is_clear():
#       move()
#   else:
#       jump()

# -----------------------------------------------------------------------------------

# Hurdle 4

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#   if front_is_clear():
#       move()
#   else:
#       jump()
