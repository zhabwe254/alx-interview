## Overview
This project is part of the ALX Software Engineering curriculum. It focuses on creating a Python script that parses log data from stdin, computes metrics, and displays statistics. The script is designed to handle real-time data streams and provide periodic reports on file sizes and HTTP status code frequencies.

## Author
- **Gideon Habwe**
- ALX Software Engineering Student

## Project Description
The log parsing script reads input from stdin line by line, processes log entries in a specific format, and computes the following metrics:
- Total file size
- Count of HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500)

The script prints these statistics every 10 lines and when interrupted by CTRL+C (SIGINT).

## Features
- Real-time processing of log data
- Periodic reporting of statistics
- Handling of keyboard interrupts (CTRL+C)
- Skipping of improperly formatted log lines
- Ascending order display of status codes

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Usage
1. Ensure the script is executable:
chmod +x 0-stats.py

2. Run the script with input piped from a log generator or file:
./0-generator.py | ./0-stats.py

cat access.log | ./0-stats.py

## Input Format
Each line of input should match the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

...

## Notes
- The script handles keyboard interruptions gracefully, printing final statistics before exiting.
- Invalid input lines are skipped without affecting the metrics.
- Only status codes present in the input are displayed in the output.

## Learning Objectives
Through this project, students will gain experience in:
- Parsing and processing data streams in real-time
- Handling I/O operations in Python
- Implementing signal handling for graceful interrupts
- Working with dictionaries and data aggregation
- Error handling and input validation

## Repository
- GitHub repository: [alx-interview](https://github.com/zhabwe254/alx-interview)
- Directory: 0x03-log_parsing
- File: 0-stats.py
