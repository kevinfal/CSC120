"""
    File: join_pieces.py
    Author: Kevin Falconett
    Purpose: join puzzle pieces together
            left to right or top to bottom
"""


def join_pieces_LR(left, right):
    """
        Joins pieces horizontally

        Parameters:
            left (list[str]): List of strings,
                             Represents a "puzzle piece"
            right (list[str]): List of strings,
                               same format as left
        
        Preconditions:
            Left and right share one side in common
            i.e: left(right) == right(left)

        Returns:
            left and right merged horizontaly
    """
    returned = []

    top = left[0] + right[0]
    returned.append(top)
    for i in range(1, len(left) - 1):
        returned.append(left[i] + right[i])

    bottom = left[-1] + right[-1]
    returned.append(bottom)

    return returned


def printList(lis):
    """
        Prints a the contents
        of a list

        Parameters:
            lis (list): list of elements
        
        Returns:
            void
    """
    for x in lis:
        print(x)


def join_pieces_TB(top, bot):
    """
        Joins pieces top to bottom by
        checking which piece should be
        on top and adding them to each
        other
        
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
    """

    # gets the top and bottom values
    # of both top and bot
    top_top = top[0]
    top_bottom = top[-1]

    bot_top = bot[0]
    bot_bottom = bot[-1]

    # decides which piece should be on top, and which should be on bottom
    if top_top == bot_bottom:
        return bot + top
    elif top_bottom == bot_top:
        return top + bot


def main():
    l = [" abc ", "d   g", "e   h", "r   i", " 123 "]
    r = [" 123 ", "g   4", "h   5", "i   6", " 789 "]
    resTB = join_pieces_TB(l, r)
    resLR = join_pieces_LR(l, r)

    print("Top and Bottom")
    printPuzz(resTB)
    print("Left and Right")
    printPuzz(resLR)


if __name__ == "__main__":
    main()
