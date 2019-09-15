"""
    File: square.py
    Author: Kevin Falconett
    Purpose: constructs a "square"
             a list of length size
             with lists of length size
    
"""


def square(size, start, inc):
    """
        constructs a 2d list of length size
        with each list of length size

        Parameters:
            size (int): length of 2d list and
                        lists it contains

            start : starting value, can be
                    string or int
            
            inc: value to increment by
                 string or int

        Returns:
            2d list of length size with
            lists of length size

    """

    returned = []

    # values to start the lists with
    values = []

    # value to be added
    added = start

    for i in range(size):
        values.append(added + inc * i)

    for i in range(size):
        added = values[i]
        returned.append([])
        
        for i2 in range(size):
            if i2 != 0:
                added += inc
            returned[i].append(added)

    return returned


def main():
    pass


if __name__ == "__main__":
    main()
