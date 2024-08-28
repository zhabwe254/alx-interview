#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter
of an island represented in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A rectangular grid where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Check if the cell above is also land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check if the cell to the left is also land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
