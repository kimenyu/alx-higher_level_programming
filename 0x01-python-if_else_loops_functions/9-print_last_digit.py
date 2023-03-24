#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    last_digit = -digit
    if number < 0:
        return last_digit
    elif number == 0:
        return digit
    else:
        return digit
