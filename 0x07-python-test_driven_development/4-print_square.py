#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): size is the size length of the square
        If type(size) is not int, raise 
        TypeError('size must be an integer'). if size < 0,
        raise ValueError('size must be >= 0), if size isinstance(float)
        raise TypeError('size must be an integer)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("{}".format("#"), end="")
        print("")
