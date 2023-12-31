def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):  # High-Order-Function, takes a function as input and uses it with given input
    return func(n1, n2)


result = calculator(2, 3, add)
print(result)  # 5

result = calculator(2, 3, multiply)
print(result)  # 6
