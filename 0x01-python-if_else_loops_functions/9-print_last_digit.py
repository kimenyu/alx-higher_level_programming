#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    last_digit = -digit
    if last_digit < 0:
        return last_digit
    else:
        return digit
