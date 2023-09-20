# Write a csv "squirrel_count" with pandas module including squirrel count with fur_color (black, grey, cinnamon)

import pandas

whole_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = whole_data["Primary Fur Color"]

fur_colors_to_search = ["Gray", "Black", "Cinnamon"]
data = {"Fur Color": fur_colors_to_search,
        "Count": []}

for color in fur_colors_to_search:
    counter = 0
    for fur in fur_colors:
        if color == fur:
            counter += 1

    data["Count"].append(counter)

data_frame = pandas.DataFrame(data)
data_frame.to_csv("squirrel_count.csv")
