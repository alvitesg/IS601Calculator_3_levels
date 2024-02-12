# calculator/calculation.py
"""Module containing the Calculation class."""

class Calculation:
    """Class to perform calculations."""

    def __init__(self, num1, num2, operation):
        """Initialize Calculation with two numbers and an operation function."""
        self.num1 = num1
        self.num2 = num2
        self.operation = operation  # Store the operation function

    def get_result(self):
        """Perform calculation and return result."""
        # Call the stored operation with num1 and num2
        return self.operation(self.num1, self.num2)
