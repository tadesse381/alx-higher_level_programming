#!/usr/bin/env python3

from random import randint

number = randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit

if digit > 5:
    message = "greater than 5"
elif digit == 0:
    message = "0"
else:
    message = "less than 6 and not 0"

print(f"Last digit of {number} is {digit} and is {message}")
