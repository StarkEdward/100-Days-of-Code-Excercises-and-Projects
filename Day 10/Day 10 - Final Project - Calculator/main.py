# Calculator
from art import logo

print(logo)


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


# creating Dictionary for operations  key as symbol and values as function
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = int(input("Enter First number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        chosen_operator = input("Choose an operation: ")
        num2 = int(input("Enter another number: "))

        calculation_function = operations[chosen_operator]
        answer = calculation_function(num1, num2)
        print(f"{num1} {chosen_operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
