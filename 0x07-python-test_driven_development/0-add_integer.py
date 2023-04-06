#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
    - a (int or float): The first number.
    - b (int or float): The second number. Default is 98.

    Returns:
    - int: The addition of a and b.

    Raises:
    - TypeError: If a or b are not integers or floats.
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
    	raise TypeError("or b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Perform the addition and return the result as an integer
    result = a + b
    if not isinstance(result, int):
        raise TypeError("Result must be an integer")
    return result
