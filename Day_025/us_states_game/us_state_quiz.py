# Creating an us-state-game using turtle and pandas
# saving remaining states into csv data
from turtle import Screen
from state import State
import pandas


screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("./game_data/blank_states_img.gif")

data = pandas.read_csv("./game_data/50_states.csv")
data_dict = data.to_dict()

states = data["state"].tolist()
x_cor = data["x"].tolist()
y_cor = data["y"].tolist()
# print(states)

counter = 0
state_input = ""
game_is_on = True

while game_is_on:

    if counter != 50:
        state_input = screen.textinput(title=str(counter) + "/50 States Correct", prompt="What's another states name?")
    else:
        game_is_on = False

    if state_input == "exit" or state_input == "quit":
        game_is_on = False

    if state_input.title() in states:
        counter += 1
        index = states.index(state_input.title())

        x = x_cor[index]
        y = y_cor[index]

        states.pop(index)
        x_cor.pop(index)
        y_cor.pop(index)

        State(x=x, y=y, name=state_input.title())

data_to_csv = {"state": states,
               "x": x_cor,
               "y": y_cor}

data_frame = pandas.DataFrame(data_to_csv)
data_frame.to_csv("states_left.csv")
screen.exitonclick()
