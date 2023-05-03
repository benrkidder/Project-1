# Import sys Module for Error Handling
import sys


# Add List of Values Together
def add(values):
    return sum(values)


# Subtract List of Values from Each Other
def subtract(values):
    difference = values[0]
    for val in values[1:]:
        difference -= val
    return difference


# Multiply List of Values Together
def multiply(values):
    product = 1
    for value in values:
        product *= value
    return product


# Divide List of Values from Each Other
def divide(values):
    quotient = values[0]
    for value in values[1:]:
        if value == 0:
            sys.exit("Cannot divide by 0")
        else:
            quotient /= value
    return quotient
