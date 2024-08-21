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
    
    # Create a list to store the minimum number of coins needed for each value
    dp = [float('inf')] * (total + 1)
    
    # No coins are needed to make 0 total
    dp[0] = 0
    
    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update dp[amount] if using the current coin reduces the number of coins
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, it means we cannot make the total
    return dp[total] if dp[total] != float('inf') else -1
