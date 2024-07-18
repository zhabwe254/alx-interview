#!/usr/bin/python3

import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the computed statistics"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status]:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """Handle CTRL+C signal"""
    print_stats()
    sys.exit(0)

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        
        # Parse the line
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            
            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            # Skip lines that don't match the expected format
            continue
        
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle CTRL+C
    print_stats()
    sys.exit(0)

# Print final stats
print_stats()
