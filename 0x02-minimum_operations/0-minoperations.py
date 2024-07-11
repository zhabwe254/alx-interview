#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n 'H'
    characters in a file.

    Args:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations needed, or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
