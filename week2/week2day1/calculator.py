def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def float_division(a, b):
    return a / b


def integer_division(a, b):
    return a // b

def modulo(a, b):
    if(b == 0):
        return "You can't divide by zero!"
    else:
        return a % b