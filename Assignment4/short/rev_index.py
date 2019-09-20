'''
    File: rev_index.py
    Author: Kevin Falconett
    Purpose: creates a dictionary with
             a words end phonemes and
             first phonemes.
'''

def build_rev_index(fileobj):
    '''
        Takes a file (pronunciation
        dictionary) returns a dictionary
        containing the last phonemes and
        all of the first phonemes
        associated with that phoneme

        Parameters:
            fileobj (file): file object
                            recieved from open()
        
        returns:
            dict(last phoneme: first phonemes)
            with first phonemes being a set
    '''

    returned = {}

    first = True
    for line in fileobj:

        # skips first line
        if first:
            first = False
            continue
        
        line = line.strip('\n')
        if(line == ''):
            continue
        
        
        line = line.split(' ')
        line.remove('')

        last_phoneme = line[-1]
        first_phoneme = line[1]

        # if the last phoneme is in dict
        if last_phoneme in returned.keys():
            #add to existing
            returned[last_phoneme].add(first_phoneme)
        else:
            #construct new set + add
            returned[last_phoneme] = set([first_phoneme])

    return returned    

def main():
    file = open(input("File: "))
    result = build_rev_index(file)
    print(result)

if __name__ == '__main__':
    main()