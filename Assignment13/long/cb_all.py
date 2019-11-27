"""
    File: cb_all.py
    Author: Kevin Falconett
    Purpose: Provides cb_all and helper functions which find
             all of the solutions for a cracker barrel peg puzzle
"""

from moves import *
from copy import deepcopy
from utility import *
from cb_one import check_solved

def cb_all(size,config):
    """
        Main function for finding all solutions for a
        given peg puzzle

        Parameters:
            size (int): size of board
            config (str): configuration of board to solve
    """
    board = list(config)
    flag,solutions = cb_all_h(size,board)
    returned = set()
    if flag:
        for solution in solutions:
            returned.add(str(solution))
        return returned
    else:
        return None

def cb_all_h(size: int, config: str):
    """
        Helper function for cb_all, finds all
        of the possible solutions for a given board and
        returns them as a list

        Parameters:
            size (int): size of the board
            config (str): str of '1's and '0's representing board

        Returns:
            Moves, List(List(Tuple)) - Lists of Lists of Tuples(Moves) that
            solve the peg puzzle
    """

    # check if solved
    if check_solved(config):
        return (True, [[]])
    
    else:
        # paths that result in a solution
        paths = []
        # get all moves possible
        moves = all_legal_moves(size,config)

        if len(moves) == 0:
            return (False,[])
        for move in moves:
            # perfom move
            do_move = update_board(deepcopy(config), move)
            found, taken = cb_all_h(size, do_move)
            if found:
                # found a solution
                for sub in taken:
                    sub.insert(0,move)
                paths += taken

        if len(paths) != 0:
            # paths is not empty
            return (True,paths)
        else:
            return (False,[])

def main():
    s = 4
    config = '0010100010'
    print(cb_all(s,config))

if __name__ == "__main__":
    main()