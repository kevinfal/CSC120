"""
    File: get_diag2.py
    Author: Kevin Falconett
"""

def get_diag2(grid: list):
    if len(grid) <= 0:
        return []
    else:
        returned = [grid[0][len(grid) - 1]]
        grid = grid[1:]
        returned.extend(get_diag2(grid))
    return returned

