'''
    File: square.py
    Author: Kevin Falconett
'''

def square(size, start, inc):
    
    returned = []
    values = []

    added = start
    for i in range(size):
        values.append(added + inc * i)

    for i in range(size):
        added = values[i] - 2
        returned.append([])
        for i2 in range(size):
            added += inc
            returned[i].append(added)
        
    return returned

def main():
    inp = input()
    sq = square(size,start,inc)
    print(sq)


if __name__ == '__main__':
    main()