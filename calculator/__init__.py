"""Module providing basic arithmetic operations."""
# calculator/__init__.py

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(num1,num2):
        """Add numbers and return value"""
        calculation = Calculation(num1, num2, add)  
        return calculation.get_result()
    @staticmethod
    def subtract(num1,num2):
        """Subtract numbers and return value"""
        calculation = Calculation(num1, num2, subtract)  
        return calculation.get_result()
    @staticmethod
    def multiply(num1,num2):
        """Multiply numbers and return value"""
        calculation = Calculation(num1, num2, multiply)  
        return calculation.get_result()
    @staticmethod
    def divide(num1,num2):
        """Divide numbers and return value"""
        calculation = Calculation(num1, num2, divide)  
        return calculation.get_result()
