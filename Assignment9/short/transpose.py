"""
    File: transpose.py
    Author: Kevin Falonett
"""

def transpose(grid):
    if len(grid) <= 0:
        return []
    elif len(grid[0]) <= 0:
        return []
    else:
        returned = [get_col(grid,0)]
        grid = remove_first_col(grid)
        returned.extend(transpose(grid))
        return returned

def remove_first_col(grid):
    if len(grid) <= 0:
        return []
    else:
        returned = [grid[0][1:]]
        returned.extend(remove_first_col(grid[1:]))
        return returned


def get_col(grid,index):
    if len(grid) <= 0:
        return []
    else:
        returned = [grid[0][index]]
        returned.extend(get_col(grid[1:],index))
        return returned
        
    return returned

