from os import system, name
from art import logo


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux
    else:
        _ = system("clear")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(num1):
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation:\n")
    num2 = float(input("What's the next number?:\n"))

    result = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    continue_calculating = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n"
    ).lower()

    if continue_calculating == "y":
        calculate(result)
    else:
        clear()
        new_calculator()


def new_calculator():
    print(logo)

    calculate(float(input("What's the first number?:\n")))


new_calculator()
