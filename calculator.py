import math

"""
calculator.py
- Defines functions used to create a simple calculators
cd 
One function per operation, in order.
"""
# First example

def add(a: float, b: float): 
    return a + b

def sub(a: float, b: float):
    return a - b

def mul(a: float, b: float):
    return a * b

def div(a: float, b: float):
    if a == 0:
        raise ZeroDivisionError
    
    else:
        return b / a
    
def log(a: float, b: float):
    try:
        return math.log(b, a)
    
    except:
        raise ValueError
    
def exp(a: float, b: float):
    return math.pow(a, b)