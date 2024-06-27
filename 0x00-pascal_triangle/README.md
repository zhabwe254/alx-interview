# Pascal's Triangle

## Overview

This project involves implementing a function to generate Pascal's Triangle up to `n` rows. Pascal's Triangle is a triangular array of binomial coefficients, where each number is the sum of the two directly above it.

## Function Definition

```python
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for row_num in range(n):
        row = [None for _ in range(row_num + 1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    
    return triangle
How It Works
Edge Case Handling:

If n is less than or equal to 0, the function returns an empty list.
Generating Pascal's Triangle:

Initialize an empty list triangle to store rows of Pascal's Triangle.
Iterate from 0 to n-1 to generate each row.
Row Construction:

For each row, create a list row initialized with None values.
Set the first and last element of the row to 1.
For the elements in between, calculate each element as the sum of the two elements directly above it from the previous row.
Appending Rows:

Append the constructed row to the triangle list.
Return:

Return the complete Pascal's Triangle as a list of lists.
