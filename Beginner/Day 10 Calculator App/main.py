import os
from art import logo


def cls():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


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


def calculator():
    print(logo)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = int(input("What's the first number? "))
second_number = int(input("What's the second number? "))
for sign in operations:
    print(sign)
    should_continue = True

while should_continue:
    operation_sign = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_sign]
    answer = calculation_function(first_number, second_number)
    print(f"{first_number} {operation_sign} {second_number} = {answer}")
    if input("Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
        first_number = answer
    else:
        should_continue = False
        cls()
        calculator()
        
calculator()
