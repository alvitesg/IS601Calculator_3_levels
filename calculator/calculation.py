# calculator/calculation.py
"""Module containing the Calculation class."""

class Calculation:
    """Class to perform calculations."""

    def __init__(self, a, b, operation):
        """Initialize Calculation with two numbers and an operation function."""
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        """Perform calculation and return result."""
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)
