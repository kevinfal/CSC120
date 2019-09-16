'''
    File: jigsaw.py
    Author: Kevin Falconett

'''

def read_pieces_file():
    '''
        Prompts file, reads and gets the puzzle
        width, height, and pieces
    '''
    #filename = 'puzzle03.pieces'
    filename = input("Give the puzzle name: ")
    file = open(filename)
    width = 0
    height = 0
    pieces = []

    for line in file:
        
        if line[0] == '#' or line == '\n':
            continue
        
        line = line.strip('\n')

        space = 0

        while line[space] == ' ':
            space += 1
        space -= 1
        if(space != -1):
            line = line[space:]
        
        split = line.split(' ')
        
        if len(split) < 3:
            width = int(split[0])
            height = int(split[1])
        else:
            split = split[1:]
            pieces.append(split)

    return (width,height,pieces)
    
def build_empty_board(wid,hei):
    '''
        Builds an empty board, a list of lists
        containing None (list[list[None]]) 
    '''
    returned = []
    for i in range(wid):
        added = []
        for i2 in range(hei):
            added.append(None)
        returned.append(added)
    return returned

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
                #print("piece {}".format(piece))
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

def piece_to_strs(piece):
    '''
        Creates 5 strings representing
        the puzzle piece in rows
    '''

    right = piece[1]
    left = piece[3][::-1]

    
    row1 = left[0] +'   ' +right[0]
    row2 = left[1] +'   ' +right[1]
    row3 = left[2] +'   ' +right[2]
    bottom = ' ' +piece[2][::-1] +' '
    top = ' ' +piece[0] +' '

    return [bottom,row3,row2,row1,top]

def join_LR(left, right):
    """
        Joins pieces horizontally

        Parameters:
            left (list[str]): List of strings,
                             Represents a "puzzle piece"
            right (list[str]): List of strings,
                               same format as left

        Returns:
            left and right merged horizontaly
    """
    #print("left {}".format(left))

    if left[0] == '':
        return right
    elif right[0] == '':
        return left

    L_Rside = left[3][-1] + left[2][-1] + right[1][-1]
    R_Lside = right[3][0] + right[2][0] + right[1][0]

    returned = []

    newLeft = []
    if L_Rside == R_Lside:
        for string in left:
            newLeft.append(string[:-1])
            left = newLeft
    #print("left {}".format(left))
    for i in range(len(left)):
        returned.append(left[i][:-1] + right[i])

    return returned

def join_TB(top,bot):
    """
        Joins pieces top to bottom, if one is
        empty, returns the other
        
        Parameters: 
            top (list[str]): List of strings,
                             Represents a "puzzle piece"

            bot (list[str]): List of strings, same
                             format as top

        Preconditions:
            top and bottom must have the same
            line on opposite sides
            i.e top(top) bot(bottom)

        Returns:
            top and bottom merged vertically
            (top + bot) and removes the line
            in common
    """

    if len(top) == 0:
        return bot
    elif len(bot) == 0:
        return top

    return top[:-1] + bot

def print_strs(strs):
    for x in strs:
        print(x)

def match_LR(left, right):
    """
        Checks to see if the right
        side of left can be matched
        to the left side of right

        Parameters:
            left (list[str]): List of strings

            right (list[str]): List of strings

        Preconditions:
            left and right are in the
            "puzzle" format (length 4)
        
        Returns:
            True if left's right side
            matches right's left side.
            False otherwise.
    """

    leftR_Side = left[1]
    rightL_Side = right[3]
    rightL_Side = rightL_Side[::-1]

    returned = leftR_Side == rightL_Side

    #print("Debug: left(R) {} right(L) {} == {}".format(leftR_Side,rightL_Side,returned))

    return leftR_Side == rightL_Side

def match_TB(a, b):
    """
        Checks to see if the bottom of a
        can be matched to the top of 
        bottom

        Parameters:
            a (list[str]): List of strings

            b (list[str]): List of strings

        Preconditions:
            a and b are in the
            "puzzle" format (length 4)
        
        Returns:
            True if a's bottom
            matches b's top.
            False otherwise.
    """
    # gets the bottom of a
    # and inverts it

    bottom = a[2]
    bottom = bottom[::-1]

    # gets the top of b
    top = b[0]

    #print("Debug: top {} bottom {} == {}".format(a,b,returned))

    return top == bottom

def main():
    """Queries the user for a filename, then reads that file as a list of
       jigsaw puzzle pieces; each piece is represented as a tuple of 4
       3-character strings, representing the 4 edges of the piece, staring
       at the top (with the leftmost character) and proceeding through all
       of the characters in clockwise order.

       Solves the jigsaw, and prints out a depiction of the puzzle at the
       end.
    """

    
    (wid,hei,pieces) = read_pieces_file()

    board = build_empty_board(wid,hei)
    fill_board(board, wid,hei, pieces)
    

    # TODO: comment this loop!
    output_lines = []
    for y in range(hei):
        this_row = [""]*5
        for x in range(wid):
            #print("board[{:f}][{:f}] {}".format(x,y,board[x][y]))
            #print(piece_to_strs(board[x][y]))
            this_piece = piece_to_strs(board[x][y])
            #print('this row {} this piece {}'.format(this_row,this_piece))
            this_row = join_LR(this_row, this_piece)
        output_lines = join_TB(this_row, output_lines)

    print_strs(output_lines)
    



if __name__ == '__main__':
    main()