#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.
    
    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to be met.
        
    Returns:
        int: Fewest number of coins needed to meet the total.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0
    
    # Sort the coin denominations in descending order
    coins.sort(reverse=True)
    
    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Determine the maximum number of coins of this denomination
        num_coins += total // coin
        # Reduce the total by the corresponding amount
        total %= coin
    
    # If the total is not zero, we couldn't meet it with the available coins
    if total != 0:
        return -1
    
    return num_coins
