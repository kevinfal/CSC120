'''
    File: join_pieces.py
    Author: Kevin Falconett

'''

import puzzle_match as puzzle

def join_pieces_LR(left,right):
    returned = []

    top = left[0] + right[0]
    returned.append(top)
    for i in range(1,len(left) - 1):
        returned.append(left[i] + right[i])
    
    bottom = left[-1] + right[-1]
    returned.append(bottom)

    return returned



def printPuzz(puzz):
    for x in puzz:
        print(x)

def join_pieces_TB(top,bot):
    
    top_top = top[0]
    top_bottom = top[-1]
    bot_top = bot[0]
    bot_bottom = bot[-1]

    if top_top == bot_bottom:
        return bot + top
    elif top_bottom == bot_top:
        return top + bot




def main():
    l =[' abc ',
        'd   g',
        'e   h',
        'r   i',
        ' 123 ']
    r= [' 123 ',
        'g   4',
        'h   5',
        'i   6',
        ' 789 ']
    res = join_pieces_TB(l,r)
    printPuzz(res)

if __name__ == '__main__':
    main()