'''
    File: jigsaw.py
    Author: Kevin Falconett
'''

def read(fileName):

    try:
        file = open(fileName)
    except:
        return None
    returned = []

    for line in file:
        
        if line[0] == '#' or line == '\n':
            continue
        
        line = line.strip('\n')

        split = line.split(' ')
        
        if len(split) < 3:
            returned.append(tuple(split))
        else:
            split = split[1:]
            returned.append(split)
            
    return returned
    



def main():
    #file = input("Give the puzzle name: ")
    file = 'puzzle01.pieces'
    puzzle = read(file)
    #print(puzzle)
    


if __name__ == '__main__':
    main()