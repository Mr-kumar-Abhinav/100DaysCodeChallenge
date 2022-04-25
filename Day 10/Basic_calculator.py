import os
from art import logo


def add(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# creating a dictionary where key = symbols and values = functions.
# key = '+', '-', '*', '/'
# value = add, subtraction, multiply, divide
# operation = {
#     f"{key}": f"{value}"
# }


operation = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide
}


def calcuator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue with {answer}, or type 'new' to start a new calculation or type 'exit' to quit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            calcuator()


calcuator()
