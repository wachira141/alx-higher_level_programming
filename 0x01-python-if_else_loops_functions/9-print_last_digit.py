#!/usr/bin/python3
def print_last_digit(number):
    c = number % 10
    if number < 0:
        c = (number % (-10)) * (-1)
    print(f"{c}", end="")
    return (c)
