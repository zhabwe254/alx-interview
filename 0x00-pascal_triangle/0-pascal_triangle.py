#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    
    Args:
    n (int): The number of rows in the Pascal's triangle.
    
    Returns:
    list: A list of lists of integers representing the Pascal's triangle of n.
    """
    if n <= 0:  # If n is less than or equal to 0, return an empty list
        return []
    
    triangle = [[1]]  # Initialize the triangle with the first row
    
    for i in range(1, n):  # Iterate over the remaining rows
        row = [1]  # Initialize the current row with the first element
        last_row = triangle[i - 1]  # Get the previous row
        
        for j in range(1, i):  # Iterate over the elements in the current row
            row.append(last_row[j - 1] + last_row[j])  # Calculate the current element
        
        row.append(1)  # Add the last element to the current row
        triangle.append(row)  # Add the current row to the triangle
    
    return triangle
