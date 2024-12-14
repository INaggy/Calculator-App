import math
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def sin(num1):
    return math.sin(math.radians(num1))

def cos(num1):
    return math.cos(math.radians(num1))

def power(num1, num2):
    return math.pow(num1, num2)

def square_root(num1):
    if num1 < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(num1)

def floor(num1):
    return math.floor(num1)

def ceil(num1):
    return math.ceil(num1)