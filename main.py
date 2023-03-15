# Calculator Project

# First, we'll define our functions for the calculator

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Now, we'll use a while loop to continuously get user input and perform calculations

while True:
    # Get user input
    num1 = float(input("Enter a number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter another number: "))

    # Perform the calculation based on the operator
    if operator == "+":
        print(add(num1, num2))
    elif operator == "-":
        print(subtract(num1, num2))
    elif operator == "*":
        print(multiply(num1, num2))
    elif operator == "/":
        print(divide(num1, num2))
    else:
        print("Invalid operator! Please use +, -, *, or /.")
