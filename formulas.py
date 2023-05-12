from math import pi


def add(val1: str, val2: str) -> str:
    """
    Add calculates the sum of val1 and val2
    :param val1: Value from __output
    :param val2: Value from entry_output
    :return: Returns the sum of val1 and val2--in scientific notation if more than 10 characters.
    """
    # Return formatted sum string
    value = float(val1) + float(val2)
    return f"{value:.7g}"


def subtract(val1: str, val2: str) -> str:
    """
    Subtract calculates the difference of val1 and val2
    :param val1: Minuend from __output
    :param val2: Subtrahend from entry_output
    :return: Returns the difference of val1 and val2--in scientific notation if more than 10 characters.
    """
    # Return formatted difference string
    difference = float(val1) - float(val2)
    return f"{difference:.8g}"


def modulo(val1: str, val2: str) -> str:
    """
    Modulo calculates the Remainder
    :param val1: The dividend from __output
    :param val2: The divisor from entry_output
    :return: Remainder formatted string
    """

    # Cannot divide by zero
    if float(val2) == 0:
        raise ZeroDivisionError

    # Zero numerator shortcut
    elif float(val1) == 0:
        return "0"

    # Return formatted remainder string
    value = float(val1) % float(val2)
    return f"{value:.8g}"


def multiply(val1: str, val2: str) -> str:
    """
    Multiply calculates the product of val1 and val2
    :param val1: Value from __output
    :param val2: Value from entry_output
    :return: Returns the product of val1 and val2--in scientific notation if more than 10 characters.
    """
    # Multiply by zero shortcut
    if float(val1) == 0 or float(val2) == 0:
        return "0"

    # Return formatted product string
    product = float(val1) * float(val2)
    return f"{product:.8g}"


def divide(val1: str, val2: str) -> str:
    """
    Divide calculates the quotient of val1 and val2
    :param val1: Dividend
    :param val2: Divisor
    :return: Quotient string
    """
    num1 = float(val1)
    num2 = float(val2)

    # Cannot divide by zero
    if num2 == 0:
        raise ZeroDivisionError

    # Shortcut
    elif num1 == 0:
        return "0"

    # Return formatted quotient string
    else:
        quotient = num1 / num2
        return f"{quotient:.8g}"


def circle(radius: str) -> str:
    """
    Circle calculates a circle's area based on the given radius.
    :param radius: Value from entry_output
    :return: Returns a formatted string representing the circle's area
    """
    r = float(radius)

    if r < 0:
        raise ValueError
    elif r == 0:
        return "0"
    else:
        area = (r ** 2) * pi
        return f"{area:.8g}"


def triangle(base: str, height: str) -> str:
    """
    Triangle calculates the area of a triangle with the given base and height values.
    :param base: Value from __temp_output
    :param height: Value from entry_output
    :return: Returns the calculated area of the triangle represented by a formatted string.
    """
    num1 = float(base)
    num2 = float(height)

    if num1 < 0 or num2 < 0:
        raise ValueError
    elif num1 == 0 or num2 == 0:
        return "0"

    area = (num1 * num2) * .5
    return f"{area:.8g}"
