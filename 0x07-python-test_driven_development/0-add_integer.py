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

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = int(a) + int(b)
    """
    Returns a + b as int
    """
    return result

