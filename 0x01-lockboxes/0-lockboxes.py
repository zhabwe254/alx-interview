#!/usr/bin/python3
"""Module for the canUnlockAll function."""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of lists): A list of lists where each inner list represents a box
                           and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
