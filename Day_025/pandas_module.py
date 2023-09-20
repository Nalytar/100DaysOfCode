import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
# print(data["temp"])

# same function that our day025.py writing

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].tolist()
print(temp_list)

avg = sum(temp_list) / len(temp_list)
# print(round(avg, 2))
# or
# print(round(data["temp"].mean(), 2))

# print(data["temp"].max())

# Get Data in Columns
print(data["condition"])  # has the to be same name than the column we want to address
# or
# print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
# print row with max temperature
# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
# print(monday.condition)
print(monday["temp"]*1.8 + 32)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Daniel", "James"],
    "scores": [67, 77, 91]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
