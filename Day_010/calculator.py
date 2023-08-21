from calculator_art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


print(logo)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Inserting the functions into a dictionary
# Could be used to call the function we want like
# function = operations["*"]
# function(2,3)
# we can also use operations[operation_symbol](num1, num2)
# this equals the multiply(2, 3) call of the function


def calculator():
    finished_calculating = False

    num1 = float(input("Whats the first number?: "))
    while not finished_calculating:
        for key in operations:
            print(key)

        operation_symbol = input("Pick a operation: ")
        if operation_symbol not in operations:
            print("You choose a invalid operator.")
            print("Program will be closed...")
            exit()

        num2 = float(input("Whats the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        program_mode = input(
                f"Type 'Y' to continue calculating with {answer}, "
                f"or type 'n' to start a new calculation, "
                f"or type 'x' to exit.: ").lower()
        if program_mode == "n":
            finished_calculating = True
            calculator()
        elif program_mode == "x":
            exit()
        else:
            num1 = answer


calculator()
# Calculator still without checking for the right user input or error handling like num1 = 8,7 instead of 8.7
# Only checks the operation symbol and closes the program if invalid choice
