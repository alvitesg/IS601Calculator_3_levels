'''My calculator test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract(2,2) == 0

def test_multiply():
    '''Test that multiply function works'''
    assert multiply(2,2) == 4

def test_divide():
    '''Test that division function works'''
    assert divide(2,2) == 1
