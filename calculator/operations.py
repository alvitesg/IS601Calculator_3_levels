def add(a,b):
    """Add two numbers, where a and b are numeric and a numeric number is returned"""
    return a + b

def subtract(a,b):
    """Subtract two numbers, where a and b are numeric and a numeric number is returned"""
    return a - b

def multiply(a,b):
    """Multiply two number, where a and b are numeric and a numeric number is returned"""
    return a * b

def divide(a,b):
    """Divide two numbers, where a and b are numeric, b must not be zero and a number is returned"""
    if b == 0:
        raise ValueError("Division by zero is not correct")
    return a / b