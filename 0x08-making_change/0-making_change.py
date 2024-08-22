#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): List of coin denominations.
        total (int): Target amount.

    Returns:
        int: Fewest number of coins needed to meet total.
             0 if total is 0 or less.
             -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
