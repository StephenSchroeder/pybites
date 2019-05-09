"""
Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
Have fun!
"""

def sum_numbers(numbers=None):
    sum = 0
    if numbers is None:
        numbers = range(1,101)

    for i in numbers:  #Could use python standard library's sum function instead
        sum += i
    
    return sum
    