
from moves import *

def legal_move(board, move):
    board_data = list(board)
    m1,m2,m3 = move
    if board_data[m1] == '1':
        if board_data[m2] == '1':
            if board_data[m3] == '0':
                return True
    
    return False


def all_legal_moves_interface(size, board_str):
    return all_legal_moves(size,board_str)


def all_legal_moves(size, board_str):

    moves = all_moves(size)
    returned = set()
    for move in moves:
        if legal_move(board_str,move):
            returned.add(move)
    return returned

def main():

    x = '110001100101011'
    s = 5
    

if __name__ == "__main__":
    main()