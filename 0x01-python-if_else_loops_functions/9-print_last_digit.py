#!/usr/bin/env python3

# Define function to print and return last digit of number
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
