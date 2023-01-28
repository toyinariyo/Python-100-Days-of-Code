import os
import operator
from art import logo


def cls():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def calculator():
    print(logo)


operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

first_number = float(input("What's the first number? "))
second_number = float(input("What's the second number? "))
for sign in operations:
    print(sign)
should_continue = True

while should_continue:
    operation_sign = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_sign]
    answer = calculation_function(first_number, second_number)
    print(f"{first_number} {operation_sign} {second_number} = {answer}")
    yes_or_no = input("Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    if yes_or_no.strip().lower() == "y":
        first_number = answer
    else:
        should_continue = False
        cls()
        calculator()
        
calculator()
