# udemy Course - 100 Days of Code - Python

# Functions with outputs

# def my_functions():
#     result = 3 * 2
#     return result

# An output can be stored in a variable or replaced the function call
# A function can have multiple return's, they can also be empty

# def format_name(firstname, lastname):
#     firstname = firstname.title()
#     lastname = lastname.title()
#     return firstname + " " + lastname
#
#
# print(format_name("miChAel", "kelLE"))

# Exercise 1
# Days in Month

print("Exercise 1")


def is_leap(year):
    """
    Docstrings always go in the first indented line of a function
    We need \"\"\" Three Quotation Marks \"\"\"
    We can write as many lines as we want!
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

print("----------------------------------------------")
