# N Queens

## Description
This project contains a Python script that solves the N Queens problem. The N Queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.

## Files
- `0-nqueens.py`: Python script that solves the N Queens problem

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the PEP 8 style (version 1.7.*)
- All files must be executable

## Usage
./0-nqueens.py N
CopyWhere N is an integer greater than or equal to 4.

## Output
The program prints every possible solution to the problem, with one solution per line. 
Format: `[[r, c], [r, c], [r, c], [r, c]]`
Where `r` and `c` represent the row and column, respectively, where a queen must be placed.

## Examples
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
Copy
## Error Handling
- If the user calls the program with the wrong number of arguments, it prints: `Usage: nqueens N`, followed by a new line, and exits with the status 1.
- If N is not an integer, it prints: `N must be a number`, followed by a new line, and exits with the status 1.
- If N is smaller than 4, it prints: `N must be at least 4`, followed by a new line, and exits with the status 1.

## Author
GIDEON HABWE
