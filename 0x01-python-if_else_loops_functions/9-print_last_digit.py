#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    number = int(number[-1])
    print(number, end="")
    return number
