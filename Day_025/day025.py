# udemy Course - 100 Days of Code - Python

# Using a Pandas library and work with csv

# Reading a csv file with Python
import csv

# without csv module
data = []
with open("weather_data.csv") as file:
    data.append(file.readlines())
print(data)


temperature = []
# with csv module

# Extract all temperature as int number from csv with module
with open("weather_data.csv") as file:
    data = csv.reader(file)
    for row in data:
        print(row)
        if row[1].isnumeric():
            temperature.append(int(row[1]))

    print(temperature)