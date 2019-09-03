"""
    File: swap.py
    Author: Kevin Falconett
    Function: If string input is even, swap first and second halves of string.
        if the length of the string is odd, then the first part of the string will be the portion of the string from
        the beginning to to the middle, but not including the middle character. The second part of the odd string
        contains everything after the middle character of the input string.  
        
"""


if __name__ == "__main__":

    # varables
    inputString = input("input: ")
    fHalf = ""
    sHalf = ""
    returned = ""
    length = len(inputString)
    mid = length // 2

    if length % 2 == 0:  # String inputted is even
        fHalf = inputString[0:mid]  # gets first half of inputted string and assigns it
        sHalf = inputString[mid:length]  # gets second half
        returned = sHalf + fHalf
    else:  # string is odd
        midChar = inputString[mid]
        fHalf = inputString[0:mid]
        sHalf = inputString[mid + 1 : length]
        returned = sHalf + midChar + fHalf

    print(returned)
