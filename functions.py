def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:  # Check for absolute zero
        raise ValueError("Temperature cannot be below absolute zero.")
    return (fahrenheit - 32) * 5 / 9


