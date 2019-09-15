


def fill_board(board, wid,hei, pieces):
    """Given an empty board (that is, a list-of-lists, filled with None's),
       and a set of pieces, searches to find the right pieces to fill the
       board.

       Finds the pieces by searching through the piece list, and matching
       edges to the bottom and left edge of already-found pieces.  The
       bottom edge of the puzzle is represented by "---" edges, and the left
       edge is represented by "|||" edges.  (The same is true for the right
       and top, but this function doesn't care about that.)

       This function always assumes that we have the perfect number of
       pieces to fill the board, and that there are no ambiguities; it doesn't
       do any backtracking, as it doesn't consider the possibility that it
       might ever fail to find a solution.

       When the function returns, the board has been completely populated with
       piece objects.
    """

    for y in range(0,hei):
        for x in range(0,wid):
            for i in range(len(pieces)): 
                piece = pieces[i]

                if x==0:
                    if piece[3] != "|||":
                        continue
                else:
                    left = board[x-1][y]
                    if not match_LR(left, piece):
                        continue

                if y==0:
                    if piece[2] != "---":
                        continue
                else:
                    bot = board[x][y-1]
                    if not match_TB(piece, bot):
                        continue

                board[x][y] = piece
                pieces = pieces[:i]+pieces[i+1:]
                break

            assert board[x][y] is not None, (x,y, board, pieces)



def main():
    """Queries the user for a filename, then reads that file as a list of
       jigsaw puzzle pieces; each piece is represented as a tuple of 4
       3-character strings, representing the 4 edges of the piece, staring
       at the top (with the leftmost character) and proceeding through all
       of the characters in clockwise order.

       Solves the jigsaw, and prints out a depiction of the puzzle at the
       end.
    """

    (wid,hei, pieces) = read_pieces_file()

    board = build_empty_board(wid,hei)
    fill_board(board, wid,hei, pieces)

    # TODO: comment this loop!
    output_lines = []
    for y in range(hei):
        this_row = [""]*5
        for x in range(wid):
            this_piece = piece_to_strs(board[x][y])
            this_row   = join_LR(this_row, this_piece)
        output_lines = join_TB(this_row, output_lines)

    print_strs(output_lines)



#I'm only putting this here so this stops giving me an error

