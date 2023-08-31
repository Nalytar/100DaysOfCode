import random
import turtle as tur
# import colorgram
# pip install colorgram


def random_color(color_list):
    return random.choice(color_list)


# rgb_colors = []
#
# colors = colorgram.extract("painting.jpg", 20)
# # won't upload the picture I used for this exercise, just take your own and change path
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)  # Used the module colorgram to get the list with rgb tuples

rgb_colors = [(234, 35, 108), (237, 74, 34), (154, 27, 61), (6, 148, 94), (234, 168, 39), (183, 158, 45),
              (26, 126, 194), (43, 191, 230), (85, 27, 92), (253, 223, 0), (125, 193, 73), (241, 219, 61),
              (180, 40, 101), (65, 175, 100), (212, 131, 166), (211, 58, 29)]

tommy = tur.Turtle()

tur.colormode(255)
tommy.pensize(10)
tommy.penup()
tommy.hideturtle()
tommy.speed("fastest")

tommy.setpos(-250.0, -250.0)

x_location = tommy.xcor()
y_location = tommy.ycor()

for row in range(1, 101):
    tommy.color(random_color(rgb_colors))
    tommy.dot(20)
    tommy.forward(50)

    if row % 10 == 0:
        y_location += 50
        tommy.setpos(x_location, y_location)

screen = tur.Screen()
screen.exitonclick()
