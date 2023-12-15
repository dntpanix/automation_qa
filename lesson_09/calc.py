

def add(a, b):
    return a + b

def dif(a, b):
    return a - b

def div(a, b):
    if b < 0:
        raise ValueError(f"{b} must be greater then 0")
    return a / b
