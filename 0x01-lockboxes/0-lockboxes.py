#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box
may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """takes a list of lists"""
    new_list = []
    for sublist in boxes:
        new_list.extend(sublist)
    for i in range(1, len(boxes)):
        if i in boxes[i] and new_list.count(i) < 2:
            return False
    return True
