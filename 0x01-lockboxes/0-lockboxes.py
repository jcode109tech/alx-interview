#!/usr/bin/python3 
 
def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    opened = set([0])
    stack = [0]  # Stack to store boxes to explore
    
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                stack.append(key)
    
    # Check if all boxes are opened
    return len(opened) == len(boxes)
