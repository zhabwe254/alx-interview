
0x08-making_change
Author: Gideon Habwe
This project is focused on solving the problem of determining the fewest number of coins needed to make up a given amount of money using a greedy algorithm approach or a dynamic programming method. The goal is to optimize for both efficiency and correctness while handling different sets of coin denominations.

Description
In this project, you are tasked with writing a function that takes a list of coin denominations and a total amount of money. The function will return the fewest number of coins required to make up the total amount. If it is impossible to create the total with the given coins, the function should return -1.

This problem can be applied in various scenarios such as making change in a shop, or even more abstract problems like resource allocation where you need to divide a resource into specific portions efficiently.

Prototype:
python
Copy code
def makeChange(coins, total):
coins: A list of the values of the coins in your possession.
total: The total amount you need to reach using the coins.
Returns:
The fewest number of coins needed to meet the total amount.
If the total is 0 or less, return 0.
If the total cannot be met with the available coins, return -1.
