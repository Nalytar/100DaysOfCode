# udemy Course - 100 Days of Code - Python

# dictionary
# dict = { KEY : VALUE }
# dict = {
#   KEY1 : VALUES,
#   KEY2 : VALUES
#   }

# Retrieving items from dictionary
# dict["KEY2"]

# Adding new items to dictionary
# dict["KEY3"] = VALUES

# empty dictionary
# empty_dict = {}

# Wipe an existing dictionary
# dict = {}

# Edit an item in a dictionary, only if KEY exists
# dict["KEY3"] = NEW_VALUE

# Loop through a dictionary
# for key in dict:
#   print(dict[key])

# travel_log = {
#   "France": {
#       "Paris": 4,
#       "Lille": 3,
#       "Dijon: 1,
#       },
#   "Germany": "Berlin"
#   }

# Exercise 1
# Grading Program

print("Exercise 1")

student_scores = {
    "Harry": 81,
    "Ron": 79,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

print("----------------------------------------------")

# Exercise 2
# Dictionary in List

print("Exercise 2")

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country, visits, cities):
    diary_entry = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(diary_entry)


add_new_country(country="Russia", visits=2, cities=["Moscow", "Saint Petersburg"])
print(travel_log)

print("----------------------------------------------")
