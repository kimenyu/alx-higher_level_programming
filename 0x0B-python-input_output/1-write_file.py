#!/usr/bin/python3
"""writes a string"""



def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written"""

    # Open the file in write mode and set encoding to UTF-8
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return len(num_chars_written)
