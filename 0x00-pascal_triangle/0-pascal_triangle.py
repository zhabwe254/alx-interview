#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for invalid input

    triangle = []  # Initialize the list to store rows

    for i in range(n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Calculate the middle elements based on the previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle

# Example usage:
if __name__ == "__main__":
    triangle_5 = pascal_triangle(5)
    for row in triangle_5:
        print("[{}]".format(", ".join(map(str, row))))
