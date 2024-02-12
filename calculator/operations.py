"""Module providing basic arithmetic operations."""

def add(num1,num2):
    """Add two numbers, where a and b are numeric and a numeric number is returned"""
    return num1 + num2

def subtract(num1,num2):
    """Subtract two numbers, where a and b are numeric and a numeric number is returned"""
    return num1 - num2

def multiply(num1,num2):
    """Multiply two number, where a and b are numeric and a numeric number is returned"""
    return num1 * num2

def divide(num1,num2):
    """Divide two numbers, where a and b are numeric, b must not be zero and a number is returned"""
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2
