class Calculation:
    """From ChatGPT feedback: A class to perform calculations using a specified operation function."""

    def __init__(self, a, b, operation):
        """From ChatGPT feedback: Initialize the Calculation object with two numbers and an operation function.

        Parameters:
        a (numeric): The first number.
        b (numeric): The second number.
        operation (function): The operation function to perform on a and b.
        """
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        """From ChatGPT feedback: Get the result of the calculation using the stored operation function.

        Returns:
        numeric: The result of the calculation.
        """
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)
