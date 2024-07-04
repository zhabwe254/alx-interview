#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = set()
    stack = [0]  # Start with the first box

    while stack:
        box_index = stack.pop()
        if box_index not in opened:
            opened.add(box_index)
            for key in boxes[box_index]:
                if key < n:  # Only consider keys that are valid box indices
                    stack.append(key)
    
    # Check if all boxes have been opened
    return len(opened) == n
