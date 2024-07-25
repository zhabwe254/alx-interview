# UTF-8 Validation

This project contains a Python implementation of a UTF-8 validation algorithm. The main task is to determine if a given data set represents a valid UTF-8 encoding.

## Project Overview

UTF-8 is a variable-width character encoding capable of encoding all 1,112,064 valid Unicode code points using one to four 8-bit bytes. This project implements a method to validate whether a given sequence of bytes represents a valid UTF-8 encoding.

## Files

- `0-validate_utf8.py`: Contains the implementation of the `validUTF8(data)` function.
- `0-main.py`: A main file for testing the `validUTF8` function.

## Function Prototype

```python
def validUTF8(data)

data: A list of integers where each integer represents 1 byte of data.
Returns: True if data is a valid UTF-8 encoding, else False.

Requirements

Allowed editors: vi, vim, emacs
All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
Code should use the PEP 8 style (version 1.7.x)
All files must be executable

Usage
To test the validUTF8 function, you can use the provided 0-main.py file:
bashCopy./0-main.py
Example
pythonCopyvalidUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Should print: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Should print: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Should print: False
Author:
Gideon Habwe
