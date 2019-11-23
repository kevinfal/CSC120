
def update_board(board: list,mov: tuple):
    m1,m2,m3 = mov
    board[m1] = '0'
    board[m2] = '0'
    board[m3] = '1'
    return ''.join(board)

def update_board_interface(board_str, mov):
    board = list(board_str)
    return update_board(board,mov)