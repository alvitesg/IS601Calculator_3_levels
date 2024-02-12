"""Module providing basic arithmetic operations."""
# calculator/__init__.py
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        """Add numbers and return value"""
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        """Subtract numbers and return value"""
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()
    @staticmethod
    def multiply(a,b):
        """Multiply numbers and return value"""
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        """Divide numbers and return value"""
        calculation = Calculation(a, b, divide)
        return calculation.get_result()
