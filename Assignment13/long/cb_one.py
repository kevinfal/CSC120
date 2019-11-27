"""
    File: cb_one.py
    Author: Kevin Falconett
    Purpose: provides cb_one and helper functions
             cb_one finds a solution for a the
             cracker barrel peg puzzle
"""

from moves import *
from copy import deepcopy
from utility import *

def cb_one(size,config):
    """
        Main function for cb_one. Calls the helper function
        and gets the solution for the puzzle

        Parameters:
            size (int): size of the board
            config (str): board configuration to solve
        
        Returns:
            str - a string that contains the the moves for a solution
            for a configuration of a board
    """
    assert size >= 4
    
    flag,returned = cb_one_h(size,config)

    return str(returned)

def cb_one_h(size: int, config: str):
    """
        Helper function for cb_one, finds the
        solutions for cb_one to return

        Parameters:
            size (int): size of the board
            config (str): str of '1's and '0's representing board
        
        Returns:
            (bool, List(Tuple)):
                    bool - flag that signals whether a solution is found or not
                    List - List of moves that solves the puzzle given in
                           the config
    """

    if check_solved(config):
        # if the board is solved
        return (True, [])
    
    else:
        # board is not solved

        # get all moves possible for this configuration
        moves = all_legal_moves(size,config)
        if len(moves) == 0:
            # if empty, then not solved/dead end
            return (False,[])
        for move in moves:
            # get the board that results from the move
            do_move = update_board(deepcopy(config), move)
            # recurse
            found, taken = cb_one_h(size, do_move)

            if not found:
                continue
            else:
                taken = [move] + taken
                return (True, taken)

    return (True,taken)

def check_solved(board:str):
    """
        Checks if a board is solved, counts
        the amount of 1s present in the string

        Paramters:
            board (str) - Configuration of board (1's and 0's)

        Returns:
            True if board str only has one '1', which means its solved
            False otherwise
    """
    count = board.count('1')
    return count == 1


def main():
    
    s = 4
    config = '001110101100111'
    print(cb_one(s,config))

if __name__ == "__main__":
    main()