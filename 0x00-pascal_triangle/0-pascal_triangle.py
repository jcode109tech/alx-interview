#!/bin/python3

def pascal_triangle(n):
    """
    This will generate the triangle, based on the 
    value n representing the num_rows
    """
    if n <= 0:
        return []
    
    # The 1st elemt of the triangle is always 1
    triangle = [[1]] 

    for i in range(1, n):
        # Each row starts with 1
        row = [1] 

        for j in range(1,i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # Each row ends with 1
        row.append(1)

        triangle.append(row)

    return triangle
