# Island Perimeter

This project implements a function to calculate the perimeter of an island represented by a grid. 

## Function
- `def island_perimeter(grid):`: Returns the perimeter of the island.

## Grid Representation
- The grid is a list of lists where:
  - `0` represents water.
  - `1` represents land.
- Each cell is square with side length 1.
- Cells are connected horizontally or vertically (not diagonally).

### Example:
Given the grid:
[ [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0] ]

bash
Copy code

The function will return: `12`
