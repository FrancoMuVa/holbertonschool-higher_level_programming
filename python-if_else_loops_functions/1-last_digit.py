#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]

if number < 0 and int(last_digit) != 0:
    last_digit = "-" + last_digit

if int(last_digit) > 5:
    str = "and is greater than 5"
elif int(last_digit) == 0:
    str = "and is 0"
elif int(last_digit) < 6:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {str}")
