
from moves import *

def legal_move(board, move):
    board_data = list(board)
    m1,m2,m3 = move
    if board_data[m1] == '1':
        if board_data[m2] == '1':
            if board_data[m3] == '0':
                return True
    
    return False


def legal_move_interface(size, board_str):
    return legal_move(size,board_str)

def main():

    x = '110001100101011'
    s = 5
    print(legal_move_interface(s,x))
    

if __name__ == "__main__":
    main()