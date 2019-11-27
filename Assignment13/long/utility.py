"""
    File: utility.py
    Author: Kevin Falconett
    Purpose: provides utility functions
"""

from moves import *

def legal_move(board, move):
    """
        Determines whether a move is legal or not

        Returns True if valid, false otherwise
    """
    board_data = list(board)
    m1,m2,m3 = move
    if board_data[m1] == '1':
        if board_data[m2] == '1':
            if board_data[m3] == '0':
                return True
    
    return False

def all_legal_moves(size, board_str):
    """
        Returns all possible moves that can be performed

        Returns List of Tuple(moves) that can be performed
    """
    moves = all_moves(size)
    returned = set()

    for move in moves:
        if legal_move(board_str,move):
            returned.add(move)
    return returned


def update_board(board: str,mov: tuple):
    """
        Perfomres the move (mov) onto board
        and returns the board
    """
    board = list(board)
    m1,m2,m3 = mov
    board[m1] = '0'
    board[m2] = '0'
    board[m3] = '1'
    return ''.join(board)
