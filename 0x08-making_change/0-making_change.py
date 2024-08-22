#!/usr/bin/python3
"""
Module for making change problem
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin values.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for efficiency
    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        coin_count += total // coin
        total %= coin

    return coin_count if total == 0 else -1
