'''
    File: puzzle_match
    Author: Kevin Falconett
'''

def puzzle_match_LR(left,right):
    
    leftR_Side = left[1]
    rightL_Side = right[3]
    rightL_Side = rightL_Side[::-1]

    return leftR_Side == rightL_Side

def puzzle_match_TB(a,b):
    bottom = a[2]
    bottom = a[::-1]
    top = b[0]
    return top == bottom

def main():
    pass

if __name__ == '__main__':
    main()