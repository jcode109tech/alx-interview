#!/usr/bin/python3

from typing import List

def island_perimeter(grid) -> int:
    sum =  0
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] == 1):
                if (i < 0 or grid[i - 1][j] == 0):
                    sum += 1


    return sum