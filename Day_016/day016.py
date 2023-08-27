# udemy Course - 100 Days of Code - Python

# Object-Oriented Programing

# Call Methods, Classes and Variables from different modules with a module name
# import turtle
# timmy = turtle.Turtle()

# Call Methods, Classes and Variables from different modules without a module name
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")  # Look into turtle graphics documentation | https://docs.python.org/3/library/turtle.html
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)  # call of an attribute | object.attribute
# my_screen.exitonclick()  # call of a methods | object.method()


# install a package over STRG + ALT + S, 'Project Name', Python Interpreter and search for package to install

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon-Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
