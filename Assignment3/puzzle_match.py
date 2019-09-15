"""
    File: puzzle_match
    Author: Kevin Falconett
    Purpose: check if puzzle pieces
            can be joined left to right
            or top to bottom
"""


def puzzle_match_LR(left, right):
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

    return leftR_Side == rightL_Side


def puzzle_match_TB(a, b):
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
    bottom = a[::-1]

    # gets the top of b
    top = b[0]

    return top == bottom


def main():
    pass


if __name__ == "__main__":
    main()
